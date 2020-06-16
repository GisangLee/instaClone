from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    web_site = models.URLField(blank=True)
    bio = models.TextField(blank=True)
