# Generated by Django 5.0 on 2025-01-16 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_remove_educationofemployee_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='education',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.educationofemployee'),
        ),
    ]
