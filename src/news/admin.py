from django.contrib import admin
from .models import News, FAQ
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class NewsAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = News
        fields = '__all__'


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


class FAQAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = FAQ
        fields = '__all__'


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    form = FAQAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Holati', {'fields': ('is_active',)}),
    )
