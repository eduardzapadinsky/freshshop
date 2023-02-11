from django.contrib import admin

from .models import Product


@admin.register(Product)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "count"]
