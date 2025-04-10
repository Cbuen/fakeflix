# Create your models here.
from django.db import models


class AuthUser(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define primary key
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


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
