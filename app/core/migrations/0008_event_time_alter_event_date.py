# Generated by Django 4.2 on 2023-11-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_document_attachment_alter_document_summary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
