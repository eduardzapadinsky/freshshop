from datetime import datetime

from django.db import models

from product.models import Product
from user.models import UserModel


class Order(models.Model):
    """
    Model for shop order
    """
    user: str = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product: str = models.ForeignKey(Product, on_delete=models.CASCADE)
    count: float = models.DecimalField(max_digits=7, decimal_places=2)
    created: datetime = models.DateTimeField(auto_now_add=True)


class Refund(models.Model):
    """
    Model for refunding shop products
    """

    order: str = models.OneToOneField(Order, on_delete=models.CASCADE)
    created: datetime = models.DateTimeField(auto_now_add=True)
