from django.contrib import admin
from . import models

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_special', 'discount']

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Category)

