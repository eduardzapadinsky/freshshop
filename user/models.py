from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    """
    Model for shops user
    """

    wallet: float = models.DecimalField(max_digits=7, decimal_places=2, default=10000)
