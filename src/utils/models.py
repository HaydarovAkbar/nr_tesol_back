from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import uuid
import os
from decimal import Decimal

User = get_user_model()


class LanguageManager(models.Manager):
    def get_queryset(self):
        return super(LanguageManager, self).get_queryset().filter(is_active=True)


class Language(models.Model):
    name = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    is_active = models.BooleanField(default=True)

    objects = LanguageManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'
        verbose_name = 'Language'
        db_table = 'languages'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Language, self).save(*args, **kwargs)
        return self


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    image = models.ImageField(upload_to='about', verbose_name='Rasm [image]', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(About, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Biz haqimizda')
        verbose_name = _('Biz haqimizda')
        db_table = 'about'


class Settings(models.Model):
    logo = models.ImageField(upload_to='settings', verbose_name='Rasm [logo]', null=True, blank=True)
    telegram = models.URLField(verbose_name='Telegram [url]', null=True, blank=True)
    instagram = models.URLField(verbose_name='Instagram [url]', null=True, blank=True)
    facebook = models.URLField(verbose_name='Facebook [url]', null=True, blank=True)
    twitter = models.URLField(verbose_name='Twitter [url]', null=True, blank=True)
    youtube = models.URLField(verbose_name='Youtube [url]', null=True, blank=True)
    whatsapp = models.CharField(verbose_name='Whatsapp [text]', null=True, blank=True, max_length=255)
    phone1 = models.CharField(verbose_name='Phone 1 [text]', null=True, blank=True, max_length=15)
    phone2 = models.CharField(verbose_name='Phone 2 [text]', null=True, blank=True, max_length=15)
    mail = models.CharField(verbose_name='Mail [text]', null=True, blank=True, max_length=25)
    address1 = models.CharField(verbose_name='Address [text]', null=True, blank=True, max_length=355)
    address2 = models.CharField(verbose_name='Address [text]', null=True, blank=True, max_length=355)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.logo.url if self.logo else ''

    class Meta:
        verbose_name_plural = _('Sozlamalar')
        verbose_name = _('Sozlamalar')
        db_table = 'settings'


class Partners(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    logo = models.ImageField(upload_to='partners', verbose_name='Rasm [logo]', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Partners')
        verbose_name = _('Partners')
        db_table = 'partners'


class Testimonials(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    image = models.ImageField(upload_to='partners', verbose_name='Rasm [logo]', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Testimonials')
        verbose_name = _('Testimonials')
        db_table = 'testimonials'


class SolidFeature(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [name]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('SolidFeature')
        verbose_name = _('SolidFeature')
        db_table = 'solid_feature'


class DottedShape(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [name]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    image = models.ImageField(upload_to='partners', verbose_name='Rasm [logo]', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Dotted Shape')
        verbose_name = _('Dotted Shape')
        db_table = 'dotted_shape'


# Faol elementlar uchun umumiy manager
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


# Nashr etilgan kurslar uchun
class PublishedCourseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=True,
            is_published=True,
            published_at__lte=timezone.now()
        )


# User progress uchun
class ProgressManager(models.Manager):
    def completed(self):
        return self.filter(status='completed')

    def in_progress(self):
        return self.filter(status='in_progress')


class TimestampedModel(models.Model):
    """Vaqt maydonlari uchun abstract model"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))

    class Meta:
        abstract = True


class StatusModel(models.Model):
    """Holat maydonlari uchun abstract model"""
    is_active = models.BooleanField(default=True, verbose_name=_("Faol"))

    class Meta:
        abstract = True


class OrderedModel(models.Model):
    """Tartib uchun abstract model"""
    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib raqami"))

    class Meta:
        abstract = True
        ordering = ['order']


class UUIDModel(models.Model):
    """UUID uchun abstract model"""
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID")
    )

    class Meta:
        abstract = True