from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid
from django.core.validators import FileExtensionValidator


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

    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib raqami [order]"))

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

    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib raqami [order]"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Courses')
        verbose_name = _('Courses')
        db_table = 'tesol_courses'


class Accreditation(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    image = models.ImageField(upload_to='accreditation', verbose_name='Rasm [image]', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Accreditation')
        verbose_name = _('Accreditation')
        db_table = 'tesol_accreditations'


class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name='Tarkibi [content]', null=True, blank=True)
    image = models.ImageField(upload_to='services', verbose_name='Rasm [image]', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Services')
        verbose_name = _('Services')
        db_table = 'tesol_services'


class GalleryCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Kategoriya nomi [title]"))
    description = models.TextField(verbose_name='Tavsifi [description]', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL slug [slug]')

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')
    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib raqami [order]"))

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Gallery kategoriyalari')
        verbose_name = _('Gallery kategoriyasi')
        db_table = 'tesol_gallery_categories'
        ordering = ['order', 'title']


class Gallery(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', _('Rasm')),
        ('video', _('Video')),
        ('file', _('Fayl')),
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID [uuid]')
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha [title]"))
    description = models.TextField(verbose_name='Tavsifi [description]', null=True, blank=True)

    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES,
        default='image',
        verbose_name='Media turi [media_type]'
    )

    image = models.ImageField(
        upload_to='gallery/images/',
        verbose_name='Rasm [image]',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp'])]
    )

    video_file = models.FileField(
        upload_to='gallery/videos/',
        verbose_name='Video fayl [video_file]',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'webm'])]
    )

    video_url = models.URLField(
        verbose_name='Video URL (YouTube, Vimeo) [video_url]',
        null=True,
        blank=True,
        help_text="YouTube yoki Vimeo video havolasi"
    )

    file_url = models.FileField(
        upload_to='gallery/files/',
        verbose_name='Fayl [file_url]',
        null=True,
        blank=True
    )

    external_url = models.URLField(
        verbose_name='Tashqi havola [external_url]',
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        GalleryCategory,
        verbose_name=_("Kategoriya [category]"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    alt_text = models.CharField(
        max_length=255,
        verbose_name='Alt matn [alt_text]',
        null=True,
        blank=True,
        help_text="Rasm uchun alternativ matn (SEO va accessibility)"
    )

    tags = models.CharField(
        max_length=500,
        verbose_name='Teglar [tags]',
        null=True,
        blank=True,
        help_text="Vergul bilan ajratilgan teglar"
    )

    is_active = models.BooleanField(default=True, verbose_name='Holati [is_active]')
    is_featured = models.BooleanField(default=False, verbose_name='Tavsiya etilgan [is_featured]')
    order = models.PositiveIntegerField(default=0, verbose_name=_("Tartib raqami [order]"))

    view_count = models.PositiveIntegerField(default=0, verbose_name='Ko\'rilgan soni [view_count]')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Nashr sanasi [published_at]')

    def __str__(self):
        return self.title

    def get_media_url(self):
        if self.media_type == 'image' and self.image:
            return self.image.url
        elif self.media_type == 'video':
            if self.video_file:
                return self.video_file.url
            elif self.video_url:
                return self.video_url
        elif self.media_type == 'file' and self.file_url:
            return self.file_url.url
        return self.external_url

    def get_thumbnail(self):
        """Kichik rasm URL ni qaytaradi"""
        if self.image:
            return self.image.url
        return None

    def increment_view_count(self):
        """Ko'rilgan sonini oshiradi"""
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def get_tags_list(self):
        """Teglarni ro'yxat shaklida qaytaradi"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []

    class Meta:
        verbose_name_plural = _('Gallery')
        verbose_name = _('Gallery elementi')
        db_table = 'tesol_gallery'
        ordering = ['-created_at']


class GalleryView(models.Model):
    """Gallery elementlarini ko'rish statistikasi"""
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='views')
    ip_address = models.GenericIPAddressField(verbose_name='IP manzil')
    user_agent = models.TextField(verbose_name='User Agent', null=True, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _('Gallery ko\'rishlar')
        verbose_name = _('Gallery ko\'rish')
        db_table = 'tesol_gallery_views'
        unique_together = ['gallery', 'ip_address']  # Bir IP dan bir marta hisoblash
