from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age =  models.PositiveIntegerField(null=True, blank=True)
    phone_nmuber =  models.CharField(max_length=11, blank=True)
