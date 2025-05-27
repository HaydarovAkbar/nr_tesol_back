from django.contrib import admin
from .models import About, Settings, Partners, Language, SolidFeature, Testimonials, DottedShape
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class DottedShapeAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = DottedShape
        fields = '__all__'


@admin.register(DottedShape)
class DottedShapeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    form = DottedShapeAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Boshqalar', {'fields': ('is_active', 'image')}),
    )


class TestimonialsAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Testimonials
        fields = '__all__'


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    form = TestimonialsAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Boshqalar', {'fields': ('is_active', 'image')}),
    )


class SolidFeatureAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = SolidFeature
        fields = '__all__'


@admin.register(SolidFeature)
class SolidFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    form = SolidFeatureAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Boshqalar', {'fields': ('is_active',)}),
    )


class AboutAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = About
        fields = '__all__'


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


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('telegram', 'instagram', 'facebook', 'phone1', 'address1', 'address2')


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


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'attr')
