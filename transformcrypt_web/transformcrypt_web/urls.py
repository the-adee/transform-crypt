"""
URL configuration for transformcrypt_web project.

More details: https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # If you ever enable admin panel:
    # path('admin/', admin.site.urls),

    # Include routes from your core app
    path('', include('core.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
