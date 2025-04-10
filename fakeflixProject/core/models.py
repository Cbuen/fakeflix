# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login


class AuthUser(AbstractUser):
    # Fix the user_permissions clash
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="authuser_permissions",  # Custom related_name
        related_query_name="authuser",
    )

    class Meta:
        db_table = "auth_user"
        managed = True  # Changed from False to True


class Profiles(models.Model):
    user = models.ForeignKey(
        AuthUser,
        on_delete=models.CASCADE,
        to_field="id",
        related_name="profiles",
        db_column="user_id",
    )
    profile1 = models.CharField(
        max_length=255, blank=True, null=True
    )  # Profile 1 (optional)
    profile2 = models.CharField(
        max_length=255, blank=True, null=True
    )  # Profile 2 (optional)
    profile3 = models.CharField(
        max_length=255, blank=True, null=True
    )  # Profile 3 (optional)
    profile4 = models.CharField(
        max_length=255, blank=True, null=True
    )  # Profile 4 (optional)

    class Meta:
        db_table = "profiles"
