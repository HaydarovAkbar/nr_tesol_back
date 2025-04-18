# Generated by Django 5.0 on 2025-01-23 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_year', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicyear',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='classofbranch',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='documentsacademicyear',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='semester',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
