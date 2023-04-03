from django.contrib import admin
from .models import Stuff,Cart,Order

# Register your models here.

admin.site.register(Stuff)
admin.site.register(Cart)
admin.site.register(Order)