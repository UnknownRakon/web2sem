from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    name = models.CharField(blank=False, max_length=100)
    surname = models.CharField(blank=False, max_length=100)
    patronymic = models.CharField(blank=False,  null=True, max_length=100)
    age = models.IntegerField(blank=False, null=True)
    date_of_birth = models.DateField(blank=False, null=True)

    def __str__(self):
        return self.email
