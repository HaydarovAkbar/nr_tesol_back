from django.db import models
from django.utils.translation import gettext_lazy as _

# from .utils.models import ActiveManager


class Teachers(models.Model):
    fullname = models.CharField(max_length=255, verbose_name=_("To'liq ismi [name]"))
    position = models.CharField(max_length=255, verbose_name=_("lavozimi [position]"))
    avatar = models.ImageField(upload_to='teachers', verbose_name='Rasm [avatar]', null=True, blank=True)
    about = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)

    is_boss = models.BooleanField(default=False, verbose_name='Rahbar [is_boss]')
    is_staff = models.BooleanField(default=False, verbose_name='Xodim [is_staff]')
    is_active = models.BooleanField(default=False, verbose_name='Holati [is_active]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = _('Teachers')
        verbose_name = _('Teachers')
        db_table = 'teachers'


class CourseType(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=255, verbose_name=_("To'liq nomi [attr]"))
    image = models.ImageField(upload_to='course_types', verbose_name='Rasm [image]', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("URL slug"), default='default-slug')
    color = models.CharField(max_length=7, default="#007bff", verbose_name=_("Rang kodi"))
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    objects = models.Manager()
    # active_objects = ActiveManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Course type')
        verbose_name = _('Course type')
        db_table = 'course_types'


class Courses(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    image = models.ImageField(upload_to='courses', verbose_name='Rasm [image]', null=True, blank=True)
    video = models.URLField(verbose_name='Video [url]', null=True, blank=True)
    teacher = models.ManyToManyField(Teachers, verbose_name=_("Muallif [teacher]"))
    course_type = models.ForeignKey(CourseType, verbose_name=_("Kurs turi [course_type]"), on_delete=models.SET_NULL,
                                    null=True)
    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Courses')
        verbose_name = _('Courses')
        db_table = 'courses'
