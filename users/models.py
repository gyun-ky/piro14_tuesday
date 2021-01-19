from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    GENDER_CHOICES = {
        ("male", "남자"),
        ("female", "여자"),
    }

    nickname = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    birth = models.DateField(null=True)

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
