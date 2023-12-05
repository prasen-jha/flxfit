from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .manager import FlxfittUserManager
from .constants import GENDER_CHOCIES

class FlxFitUser(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOCIES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    objects = FlxfittUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["gender", "date_of_birth"]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name = "Flx Fit User"
        verbose_name_plural = "Flx Fit Users"