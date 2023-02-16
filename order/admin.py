from django.contrib import admin

from .models import Order, Refund


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin panel: Order
    """
    list_display = ["user", "product", "count", "created"]


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    """
    Admin panel: Refund
    """
    list_display = ["id", "order", "created"]
