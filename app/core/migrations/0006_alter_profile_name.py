# Generated by Django 4.2 on 2023-11-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_course_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='dupa', max_length=20, null=True, unique=True),
        ),
    ]
