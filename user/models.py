from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Disallow for user to get initial wallet money
    """

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault("wallet", 0)
        user = self.model(**extra_fields)
        user.save()
        return user


class UserModel(AbstractUser):
    """
    Model for shops user
    """

    wallet: float = models.DecimalField(max_digits=7, decimal_places=2, default=10000)

    objects = UserManager()
