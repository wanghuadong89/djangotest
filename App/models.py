from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    sex = models.BooleanField(default=True)
    age = models.IntegerField(default=20)
    icon = models.CharField(max_length=70)
    phone = models.CharField(max_length=11)
    class Meta:
        db_table = 'user'









