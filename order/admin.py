from django.contrib import admin
from . import models

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'payment', 'status', 'total_price']

admin.site.register(models.Order, CartAdmin)
admin.site.register(models.Cart)

