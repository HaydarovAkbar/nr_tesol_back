from django.db import models
from utils.models import TimestampedModel, StatusModel, OrderedModel, ActiveManager


class Planners(TimestampedModel, StatusModel, OrderedModel):
    title = models.CharField(max_length=255, verbose_name="To'liq nomi [title]")
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    image = models.ImageField(upload_to='planners', verbose_name='Rasm [image]', null=True, blank=True)

    objects = ActiveManager()

    class Meta:
        verbose_name_plural = 'Planners'
        verbose_name = 'Planner'
        db_table = 'planners'

    def __str__(self):
        return self.title
