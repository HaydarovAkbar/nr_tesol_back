# Generated by Django 5.0 on 2025-01-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_is_employee_customuser_is_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
