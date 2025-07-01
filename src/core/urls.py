from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from tesol.urls import urlpatterns as tesol_urls
from news.urls import urlpatterns as news_urls
from account.urls import urlpatterns as account_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

urlpatterns += tesol_urls + news_urls + account_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
