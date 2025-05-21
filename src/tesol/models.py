from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone
import uuid


class News(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID [uuid]')
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    published_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Yangiliklar')
        verbose_name = _('Yangilik')
        db_table = 'tesol_news'


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
        db_table = 'tesol_about'


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
        db_table = 'tesol_settings'


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
        db_table = 'tesol_teachers'


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
        db_table = 'tesol_partners'


class CourseType(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=255, verbose_name=_("To'liq nomi [attr]"))
    image = models.ImageField(upload_to='course_types', verbose_name='Rasm [image]', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Course type')
        verbose_name = _('Course type')
        db_table = 'tesol_course_types'


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
        db_table = 'tesol_courses'
