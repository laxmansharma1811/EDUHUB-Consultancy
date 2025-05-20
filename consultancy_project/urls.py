"""
URL configuration for consultancy_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Ensure settings is imported
from django.conf.urls.static import static  # Ensure static is imported

# Define your primary URL patterns first
urlpatterns = [
    path('eduhub-admin/', admin.site.urls),
    path('', include('consultancy_app.urls')),
]

# Conditionally add static and media file serving patterns
# ONLY for use during DEVELOPMENT (when DEBUG = True)
if settings.DEBUG:
    # This helps the Django development server find and serve static files
    # from your STATIC_ROOT (after you've run collectstatic) or from STATICFILES_DIRS.
    # For production, WhiteNoise (or Nginx/Apache) handles this.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # If you are also using user-uploaded media files (MEDIA_URL and MEDIA_ROOT)
    # and want the development server to serve them, add this:
    # Ensure MEDIA_URL and MEDIA_ROOT are defined in settings.py if you uncomment.
    # if getattr(settings, 'MEDIA_URL', None) and getattr(settings, 'MEDIA_ROOT', None):
    #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
