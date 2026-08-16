from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Replaces Django's default User — adds full_name, phone, and a unique email."""
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    # username + password are already provided by AbstractUser
    REQUIRED_FIELDS = ['email', 'full_name', 'phone']

    def __str__(self):
        return self.username