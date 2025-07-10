from django.contrib import admin
from .models import Planners
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class PlannersAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Planners
        fields = '__all__'


# @admin.register(Planners)
# class PlannersAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at', 'updated_at', 'is_active')
#     search_fields = ('title',)
#     list_filter = ('created_at', 'updated_at')
#     ordering = ('-created_at',)
#
#     # def has_add_permission(self, request):
#     #     return False


@admin.register(Planners)
class PlannersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_active')
    form = PlannersAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Qolganlari', {'fields': ('image',)}),
    )
