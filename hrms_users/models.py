from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .managers import HrmsUsersManager

import uuid

# Create your models here.

class HrmsUsers(AbstractUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(default=False, null=True)
    is_employee = models.BooleanField(default=False, null=True)
    status = models.BooleanField(default=False, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/', default='')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    username = None
    
    objects = HrmsUsersManager()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    