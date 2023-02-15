from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    """
    Model for shop product
    """
    name: str = models.CharField(max_length=255)
    slug: str = models.SlugField(max_length=255, verbose_name="url", unique=True)
    description: str = models.TextField(max_length=1000)
    price: float = models.DecimalField(max_digits=7, decimal_places=2)
    count: float = models.DecimalField(max_digits=7, decimal_places=2)
    picture: str = models.ImageField(upload_to="shop_gallery")

    def save(self, *args, **kwargs):
        """
        Slug autofill
        """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse("product-detail", args=[self.slug])
