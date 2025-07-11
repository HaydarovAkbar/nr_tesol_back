# Generated by Django 5.2.1 on 2025-06-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesol', '0007_accreditation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name="To'liq nomi [title]")),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name="To'liq nomi [title]")),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name="To'liq nomi [title]")),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name="To'liq nomi [title]")),
                ('content', models.TextField(blank=True, null=True, verbose_name='Tarkibi [content]')),
                ('content_uz', models.TextField(blank=True, null=True, verbose_name='Tarkibi [content]')),
                ('content_en', models.TextField(blank=True, null=True, verbose_name='Tarkibi [content]')),
                ('content_ru', models.TextField(blank=True, null=True, verbose_name='Tarkibi [content]')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services', verbose_name='Rasm [image]')),
                ('is_active', models.BooleanField(default=True, verbose_name='Holati [is_active]')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
                'db_table': 'tesol_services',
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Tartib raqami [order]'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Tartib raqami [order]'),
        ),
    ]
