from django.contrib import admin
from .models import CourseType, Courses, Teachers
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class CoursesAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    content_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Courses
        fields = '__all__'


class TeachersAdminForm(forms.ModelForm):
    about_uz = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    about_en = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    about_ru = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)

    class Meta:
        model = Teachers
        fields = '__all__'


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'avatar', 'is_boss', 'is_staff', 'is_active')
    form = TeachersAdminForm

    fieldsets = (
        ('O\'zbekcha', {'fields': ('about_uz', 'position_uz',)}),
        ('Inglizcha', {'fields': ('about_en', 'position_en',)}),
        ('Ruscha', {'fields': ('about_ru', 'position_ru',)}),
        ('Boshqalar', {'fields': ('fullname', 'avatar', 'is_boss', 'is_staff', 'is_active')}),
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
