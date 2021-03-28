from django.contrib import admin

# Register your models here.
from .models import Order
#registramos order para que aparezca en el panel
admin.site.register(Order)
