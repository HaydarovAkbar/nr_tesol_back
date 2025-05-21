from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone
import uuid


class News(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID [uuid]')
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    image = models.ImageField(upload_to='images', verbose_name='Tarkibi [image]', null=True, blank=True)

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
