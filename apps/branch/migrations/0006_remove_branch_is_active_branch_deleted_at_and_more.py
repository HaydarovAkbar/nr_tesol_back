# Generated by Django 5.0 on 2025-01-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0005_remove_branch_location_branch_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='is_active',
        ),
        migrations.AddField(
            model_name='branch',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
