from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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
