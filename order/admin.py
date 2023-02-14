from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin panel: Order
    """
    list_display = ["user", "product", "count", "created"]
