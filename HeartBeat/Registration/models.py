from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractBaseUser):
    login = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id