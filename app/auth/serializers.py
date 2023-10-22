from core.models import Profile
from core.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

ALL_PROFILES = [(i.name, i.name) for i in Profile.objects.all()]


class TokenObtainerSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


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
    profile = serializers.ChoiceField(choices=ALL_PROFILES)

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
            profile=Profile.objects.get(name=validated_data['profile'])
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
