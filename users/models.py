from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    ROLE_CHOICES = (
        ('subscriber', 'Subscriber'),
        ('author', 'Author'),
        ('admin', 'Admin')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='subscriber')
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True