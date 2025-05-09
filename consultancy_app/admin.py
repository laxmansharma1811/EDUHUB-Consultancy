from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(Consultation)
admin.site.register(PartnerApplication) 