from django.contrib.auth import authenticate
from core.models import User, Profile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all()), ]
    )
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True,
        validators=[validate_password, ]
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )
    profile = serializers.ChoiceField(
        choices=[('student', 'student'), ('organizer', 'organizer'), ('external', 'external')])

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'profile')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, obj):
        if obj['password'] != obj['password2']:
            raise ValidationError({'password': "Password fields don't match"})
        return obj

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            profile=Profile.objects.get_or_create(name=validated_data['profile'])[0]
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for login endpoint."""
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs):
        """Validate if the requested login is OK."""
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Access denied: Wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
