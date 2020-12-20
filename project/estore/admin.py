from django.contrib import admin
from .models import Item , Order ,OderItem

# Register your models here.

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OderItem)