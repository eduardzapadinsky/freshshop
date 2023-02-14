from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin panel: Product
    """
    list_display = ["name", "price", "count", "get_image"]
    readonly_fields = ["slug", "get_image"]
    fieldsets = (
        (None, {"fields": (('name', 'slug'),)}),
        (None, {"fields": ('description',)}),
        (None, {"fields": (('price', 'count'),)}),
        (None, {"fields": (('picture', 'get_image'),)}),
    )

    def get_image(self, obj):
        """
        Getting image
        """
        return mark_safe(f"<img src={obj.picture.url} height='50'")

    get_image.short_description = 'Image'
    get_image.allow_tags = True
