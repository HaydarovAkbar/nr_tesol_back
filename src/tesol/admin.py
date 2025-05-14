from django.contrib import admin
from .models import About, NewsImage, News, Settings, Partners, CourseType, Courses, Teachers


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ('news', 'image')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'published_at')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('telegram', 'instagram', 'facebook', 'phone1', 'address1', 'address2')


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'avatar', 'is_boss', 'is_staff', 'is_active')
