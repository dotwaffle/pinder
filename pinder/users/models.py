from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class Isp(models.Model):

    asn = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    isp = models.ForeignKey(Isp)

    is_staff = models.BooleanField(
        "Staff status",
        default=False,
        help_text="Designates whether the user can log into the admin site."
    )
    is_active = models.BooleanField(
        "Active",
        default=True,
        help_text="Designates whether this user should be treated as active."
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/users/%s/" % self.asn

    def get_short_name(self):
        """
        Django wants this.  Not sure why.
        """
        return self.asn

    def get_username(self):
        """
        Required by Django to use as a key for authentication.
        """
        return self.email
