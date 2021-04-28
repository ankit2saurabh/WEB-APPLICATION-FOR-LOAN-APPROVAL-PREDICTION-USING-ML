from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('project.urls')),
    path(r'', include('news.urls')),
    path(r'', include('userpower.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)