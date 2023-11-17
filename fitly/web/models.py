from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Add your additional fields here
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    birthdate = models.DateField()
    address = models.TextField()
    social_media = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='customuser_set',  # Choose a suitable related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set',  # Choose a suitable related_name
        related_query_name='user',
    )
