# Generated by Django 5.0 on 2025-01-22 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_year', '0001_initial'),
        ('branch', '0003_branch_type_organization'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='branch.branch'),
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='academic_year.classofbranch'),
        ),
        migrations.AlterField(
            model_name='parentofstudent',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='parentofstudent',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
