from django.contrib import admin

from .models import UserModel


@admin.register(UserModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["email", "wallet"]
