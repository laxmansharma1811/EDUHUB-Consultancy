import os
import sys

# --- Python Virtual Environment ---
# Path to your virtual environment's activate_this.py file.
# This is crucial for Passenger to use the correct Python interpreter and packages.
ACTIVATE_THIS = '/home/eduhubun/virtualenv/EDUHUB-Consultancy/3.9/bin/activate_this.py'

try:
    with open(ACTIVATE_THIS) as file_:
        exec(file_.read(), dict(__file__=ACTIVATE_THIS))
except FileNotFoundError:
    # Log an error if the virtual environment activation script is not found.
    # This error might appear in your cPanel error logs for the Python app.
    sys.stderr.write(f"CRITICAL ERROR: Virtual environment activation file not found at {ACTIVATE_THIS}\n")
    sys.stderr.write("Ensure the path is correct and the file exists.\n")
    # You might want to raise an exception or exit if this happens,
    # as the application likely won't run correctly.
    # For now, it will try to proceed, potentially leading to import errors.
    pass # Or raise RuntimeError("Virtualenv not found")

# --- Project Path ---
# Add your Django project's root directory to the Python sys.path.
# This is the directory containing your 'manage.py' and your project package ('consultancy_project').
PROJECT_ROOT = '/home/eduhubun/EDUHUB-Consultancy'
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# --- Django Settings Module ---
# Tell Django which settings file to use.
os.environ['DJANGO_SETTINGS_MODULE'] = 'consultancy_project.settings'

# --- WSGI Application Setup with WhiteNoise ---
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Get the underlying Django WSGI application.
_django_application = get_wsgi_application()

# Wrap the Django application with WhiteNoise.
# WhiteNoise will automatically use STATIC_ROOT and STATIC_URL from your settings.py
# to serve static files.
application = WhiteNoise(_django_application)

# Optional: If you are serving user-uploaded MEDIA files with WhiteNoise
# (generally okay for smaller sites; for larger sites, use a dedicated file server or cloud storage).
# Ensure MEDIA_ROOT and MEDIA_URL are correctly defined in your settings.py if you uncomment this.
#
# from django.conf import settings
# if getattr(settings, 'MEDIA_URL', None) and getattr(settings, 'MEDIA_ROOT', None):
#     # Ensure MEDIA_ROOT is an absolute path or correctly relative to BASE_DIR
#     media_root_path = settings.MEDIA_ROOT
#     if not os.path.isabs(media_root_path):
#         # Assuming MEDIA_ROOT in settings is relative to BASE_DIR
#         media_root_path = os.path.join(settings.BASE_DIR, media_root_path)
#
#     # Ensure the prefix for add_files doesn't start with a slash if MEDIA_URL does
#     media_url_prefix = settings.MEDIA_URL.lstrip('/')
#
#     application.add_files(media_root_path, prefix=media_url_prefix)

# The 'application' variable is what Phusion Passenger (used by cPanel's Python App)
# will look for to run your Django project.
