from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


class Account(models.Model):
    username = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    is_enable = models.BooleanField(default=True)
    # email = models.EmailField()
    # password = models.TextField() ENFhaRQAMV
    # updated_time = models.DateTimeField(auto_now=True)
    # avatar = models.ImageField(blank=True)
