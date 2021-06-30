from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
