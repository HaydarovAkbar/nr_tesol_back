from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone
import uuid


class News(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID [uuid]')
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    published_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Yangiliklar')
        verbose_name = _('Yangilik')
        db_table = 'news'
        indexes = [
            models.Index(fields=['uuid', 'is_active']),
            models.Index(fields=['title']),
        ]


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images', verbose_name='Yangilik [news]')
    image = models.ImageField(upload_to='news', verbose_name='Rasm [image]', null=True, blank=True)

    def __str__(self):
        return self.news.title

    def get_image_url(self):
        try:
            return settings.HOST + self.image.url
        except:
            return ''

    class Meta:
        verbose_name_plural = _('Yangiliklar rasmlari')
        verbose_name = _('Yangilik rasmi')
        db_table = 'news_images'


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
