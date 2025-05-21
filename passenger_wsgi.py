# passenger_wsgi.py (Your original, for production)
import os
import sys

# --- Python Virtual Environment ---
ACTIVATE_THIS = '/home/eduhubun/virtualenv/EDUHUB-Consultancy/3.9/bin/activate_this.py'
try:
    # Add a print/stderr write BEFORE activation for debugging
    sys.stderr.write("passenger_wsgi.py: Attempting to activate virtualenv...\n")
    with open(ACTIVATE_THIS) as file_:
        exec(file_.read(), dict(__file__=ACTIVATE_THIS))
    sys.stderr.write("passenger_wsgi.py: Virtualenv activation attempted.\n") # Should appear if no error in exec
except FileNotFoundError:
    sys.stderr.write(f"CRITICAL ERROR: Virtual environment activation file not found at {ACTIVATE_THIS}\n")
    # Consider raising an exception here to make the failure more obvious
    # raise RuntimeError(f"Virtualenv not found at {ACTIVATE_THIS}")
    pass
except Exception as e:
    sys.stderr.write(f"CRITICAL ERROR during virtualenv activation: {str(e)}\n") # Log other exceptions
    # raise # Re-raise the exception
    pass

# --- Project Path ---
PROJECT_ROOT = '/home/eduhubun/EDUHUB-Consultancy'
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
sys.stderr.write(f"passenger_wsgi.py: PROJECT_ROOT '{PROJECT_ROOT}' added to sys.path.\n")

# --- Django Settings Module ---
os.environ['DJANGO_SETTINGS_MODULE'] = 'consultancy_project.settings'
sys.stderr.write(f"passenger_wsgi.py: DJANGO_SETTINGS_MODULE set to '{os.environ['DJANGO_SETTINGS_MODULE']}'.\n")

# --- WSGI Application Setup with WhiteNoise ---
try:
    sys.stderr.write("passenger_wsgi.py: Attempting to import Django and WhiteNoise...\n")
    from django.core.wsgi import get_wsgi_application
    from whitenoise import WhiteNoise
    sys.stderr.write("passenger_wsgi.py: Django and WhiteNoise imported successfully.\n")

    sys.stderr.write("passenger_wsgi.py: Attempting to get Django WSGI application...\n")
    _django_application = get_wsgi_application()
    sys.stderr.write("passenger_wsgi.py: Django WSGI application obtained.\n")

    sys.stderr.write("passenger_wsgi.py: Attempting to wrap with WhiteNoise...\n")
    application = WhiteNoise(_django_application)
    sys.stderr.write("passenger_wsgi.py: Application wrapped with WhiteNoise.\n")

    # Optional MEDIA serving
    # from django.conf import settings
    # if getattr(settings, 'MEDIA_URL', None) and getattr(settings, 'MEDIA_ROOT', None):
    #     sys.stderr.write("passenger_wsgi.py: Attempting to add media files for WhiteNoise...\n")
    #     media_root_path = settings.MEDIA_ROOT
    #     if not os.path.isabs(media_root_path):
    #         media_root_path = os.path.join(settings.BASE_DIR, media_root_path)
    #     media_url_prefix = settings.MEDIA_URL.lstrip('/')
    #     application.add_files(media_root_path, prefix=media_url_prefix)
    #     sys.stderr.write("passenger_wsgi.py: Media files added for WhiteNoise.\n")

except Exception as e:
    # Catch any exception during Django/WhiteNoise setup and log it
    sys.stderr.write(f"CRITICAL ERROR during Django/WhiteNoise setup in passenger_wsgi.py: {str(e)}\n")
    # You might want to reraise the exception here to ensure Passenger sees a failure
    # or provide a fallback minimal application for Passenger.
    # For now, logging is key.
    # Fallback application to ensure Passenger doesn't hang and still reports something
    def minimal_error_app(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b"Error during Django application loading. Check server logs."]
    application = minimal_error_app
    # raise # Re-raise the exception so Passenger logs it properly

sys.stderr.write("passenger_wsgi.py: Script execution finished.\n")
