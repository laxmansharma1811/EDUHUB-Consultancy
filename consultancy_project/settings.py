"""
Django settings for consultancy_project project.
SERVER CONFIGURATION
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# It's best practice to load this from an environment variable in production.
# For now, ensure this key is strong and unique.
SECRET_KEY = 'django-insecure-h#bs9x&k(p9w^%0i2q9_xb$is*rfgdxw27%8z2hf=6sp(-l2da' # Replace with your actual strong secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # MUST be False for production
#DEBUG=True
ALLOWED_HOSTS = ['www.eduhubuniversalservices.com', 'eduhubuniversalservices.com', "*"]
# Add any other domains or subdomains that will point to this Django app.
# Example: ALLOWED_HOSTS = ['www.eduhubuniversalservices.com', 'eduhubuniversalservices.com', 'eduhubun.yourcpanelserver.com'] (if cPanel uses a temp domain)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Good for consistency if you ever toggle DEBUG locally
    'django.contrib.staticfiles',   # Manages static files
    'consultancy_app',              # Your application
    # Add any other apps here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise for serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'consultancy_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Project-level templates
        'APP_DIRS': True, # Looks for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'consultancy_project.wsgi.application' # Points to your project's wsgi.py


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Ensure this path is correct for your server environment if db.sqlite3 is in BASE_DIR
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# For production, consider using a more robust database like PostgreSQL or MySQL,
# which cPanel often provides.


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC' # Or your server's/application's preferred timezone
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/' # The URL prefix for static files, e.g., yourdomain.com/static/

# Directories where Django's 'collectstatic' will look for static files
# IN ADDITION to each app's 'static' subdirectory.
# Since your `tree` output showed no project-level 'static' folder and all assets
# were under `consultancy_app/static/assets`, we can leave this empty.
# If you create a project-level 'static' folder later, add it here:
# e.g., os.path.join(BASE_DIR, 'project_wide_static_folder')
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "static"), # We commented this out based on your `tree` output.
                                       # If you create this dir, uncomment this line.
]

# The absolute path to the directory where `collectstatic` will collect all static files
# for deployment. This is where WhiteNoise (or Apache/Nginx) will serve files from.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # All static files will be copied here

# WhiteNoise configuration for efficient static file serving (compression, cache-busting)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files (User-uploaded content like images or documents)
# If your application allows users to upload files, configure these.
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Ensure the 'media' directory exists and has correct write permissions for the web server user.
# WhiteNoise can serve these too if you uncomment the relevant lines in passenger_wsgi.py,
# but for larger sites, a dedicated solution (S3, Nginx/Apache config) is better.


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings (uncomment and configure as needed for production)
# CSRF_COOKIE_SECURE = True  # If served over HTTPS
# SESSION_COOKIE_SECURE = True # If served over HTTPS
# SECURE_SSL_REDIRECT = True # If all traffic should be HTTPS
# SECURE_HSTS_SECONDS = 31536000 # e.g., 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY' # Or 'SAMEORIGIN'
