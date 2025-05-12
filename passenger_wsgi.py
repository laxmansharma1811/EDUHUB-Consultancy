import os
import sys

# Add the project root directory to sys.path
# Keep this line - it seems necessary for your setup
sys.path.insert(0, '/home/eduhubun/EDUHUB-Consultancy')

# Set the Django settings module
# Keep this line
os.environ['DJANGO_SETTINGS_MODULE'] = 'consultancy_project.settings'

# Activate the virtual environment
# Keep this block - it's important for Passenger to use your venv
activate_this = '/home/eduhubun/virtualenv/EDUHUB-Consultancy/3.9/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Load the WSGI application
# Keep this line
from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application() # Store the original app temporarily

# ---- Add WhiteNoise wrapper ----
from whitenoise import WhiteNoise

# Create the WhiteNoise instance, wrapping the original application.
# It will automatically use STATIC_ROOT from your settings.
# Pointing root directly is often more robust in passenger_wsgi.py
static_root_path = os.path.join(os.path.dirname(__file__), 'static_root')
application = WhiteNoise(_application, root=static_root_path)

# Explicitly tell WhiteNoise about the /static/ URL prefix if needed (recommended)
application.add_files(static_root_path, prefix='static/')
# ---- End WhiteNoise wrapper ----

# The final 'application' variable is now the WhiteNoise-wrapped app
