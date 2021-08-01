from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()
# class User(AbstractUser):
#     is_rahul = models.BooleanField(default=False)
#     is_ramesh = models.BooleanField(default=False)

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    is_personal = models.BooleanField(default=False)
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table="Account"
        verbose_name="Account"
        verbose_name_plural="Account"