from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    username = models.CharField(max_length=50, unique = True)
    email = models.EmailField(null = True)
    firstName = models.CharField(null= True, max_length = 50)
    lastName = models.CharField(null= True, max_length = 50)
    profilePicture = models.ImageField(upload_to='profile')
    address = models.TextField(null= True)
    role = models.BooleanField(default = False)

    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs) -> None:
        self.email = self.email.lower()
        return super().save(*args, **kwargs)