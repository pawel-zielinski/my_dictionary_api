# Generated by Django 4.2 on 2023-10-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_tag_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attachment',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]