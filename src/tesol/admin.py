from django.contrib import admin
from .models import About, News, Settings, Partners, CourseType, Courses, Teachers, Accreditation, Services, Gallery, \
    GalleryCategory, GalleryView
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class GalleryAdminForm(forms.ModelForm):
    description_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    description_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    description_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Gallery
        fields = '__all__'


class CoursesAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Courses
        fields = '__all__'


class ServicesAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Services
        fields = '__all__'


class AboutAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = About
        fields = '__all__'


class NewsAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = News
        fields = '__all__'


class TeachersAdminForm(forms.ModelForm):
    about_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    about_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    about_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Teachers
        fields = '__all__'


class AccreditationAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Accreditation
        fields = '__all__'


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    form = AccreditationAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Boshqalar', {'fields': ('is_active', 'image')}),
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    form = AboutAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Boshqalar', {'fields': ('is_active', 'image')}),
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'published_at')
    form = NewsAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Chop etilgan vaqti', {'fields': ('published_at',)}),
        ('Holati', {'fields': ('is_active',)}),
        ('Rasm', {'fields': ('image',)}),
    )


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('telegram', 'instagram', 'facebook', 'phone1', 'address1', 'address2')


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'avatar', 'is_boss', 'is_staff', 'is_active')
    form = TeachersAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('about_uz', 'position_uz',)}),
        ('Inglizcha', {'fields': ('about_en', 'position_en',)}),
        ('Ruscha', {'fields': ('about_ru', 'position_ru',)}),
        ('Boshqalar', {'fields': ('fullname', 'avatar', 'is_boss', 'is_staff', 'is_active', 'order')}),
    )


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    form = CoursesAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Files', {'fields': ('image', 'video')}),
        ('Qolganlari', {'fields': ('teacher', 'course_type')}),
    )


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz',)}),
        ('Inglizcha', {'fields': ('title_en',)}),
        ('Ruscha', {'fields': ('title_ru',)}),
        ('Boshqalar', {'fields': ('is_active', 'attr', 'image')}),
    )


class PartnersAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Partners
        fields = '__all__'


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Boshqalar', {'fields': ('logo', 'is_active')}),
    )
    form = PartnersAdminForm


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    form = ServicesAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Boshqalar', {'fields': ('image', 'is_active')}),
    )


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order', 'title']

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description')
        }),
        (_('Sozlamalar'), {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    form = GalleryAdminForm
    list_display = [
        'title',
        'media_type',
        'category',
        'preview_image',
        'is_active',
        'is_featured',
        'view_count',
        'created_at'
    ]
    list_filter = [
        'media_type',
        'category',
        'is_active',
        'is_featured',
        'created_at',
        'published_at'
    ]
    search_fields = ['title_en', 'description_en', 'tags', 'alt_text']
    list_editable = ['is_active', 'is_featured']
    readonly_fields = ['uuid', 'view_count', 'created_at', 'updated_at', 'preview_image']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'description_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'description_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'description_ru',)}),
        (None, {
            'fields': ('category', 'media_type')
        }),
        (_('Media fayllar'), {
            'fields': ('image', 'video_file', 'video_url', 'file_url', 'external_url'),
            'description': 'Media turiga qarab tegishli maydonni to\'ldiring'
        }),
        (_('SEO va Accessibility'), {
            'fields': ('alt_text', 'tags'),
            'classes': ('collapse',)
        }),
        (_('Sozlamalar'), {
            'fields': ('is_active', 'is_featured', 'order', 'published_at')
        }),
        (_('Statistika'), {
            'fields': ('uuid', 'view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def preview_image(self, obj):
        """Admin panelda rasm preview"""
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        elif obj.media_type == 'video':
            return format_html('<span style="color: #007cba;">🎥 Video</span>')
        elif obj.media_type == 'file':
            return format_html('<span style="color: #dc3545;">📄 Fayl</span>')
        return "-"

    preview_image.short_description = _('Preview')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')

    actions = ['activate_items', 'deactivate_items', 'feature_items', 'unfeature_items']

    def activate_items(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} ta element faollashtirildi.")

    activate_items.short_description = _("Tanlangan elementlarni faollashtirish")

    def deactivate_items(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} ta element o'chirildi.")

    deactivate_items.short_description = _("Tanlangan elementlarni o'chirish")

    def feature_items(self, request, queryset):
        queryset.update(is_featured=True)
        self.message_user(request, f"{queryset.count()} ta element tavsiya etilgan qilib belgilandi.")

    feature_items.short_description = _("Tavsiya etilgan qilib belgilash")

    def unfeature_items(self, request, queryset):
        queryset.update(is_featured=False)
        self.message_user(request, f"{queryset.count()} ta elementdan tavsiya belgisi olib tashlandi.")

    unfeature_items.short_description = _("Tavsiya belgisini olib tashlash")


@admin.register(GalleryView)
class GalleryViewAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'ip_address', 'viewed_at']
    list_filter = ['viewed_at', 'gallery__category']
    search_fields = ['gallery__title', 'ip_address']
    readonly_fields = ['gallery', 'ip_address', 'user_agent', 'viewed_at']
    date_hierarchy = 'viewed_at'
    ordering = ['-viewed_at']

    def has_add_permission(self, request):
        return False  # Ko'rish statistikasini qo'lda qo'shib bo'lmaydi

    def has_change_permission(self, request, obj=None):
        return False  # Ko'rish statistikasini o'zgartirib bo'lmaydi
