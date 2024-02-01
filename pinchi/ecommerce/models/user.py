from django.db import models
from django.utils.translation import gettext_lazy as _
from .department import Department
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    # Override the groups field
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="ecommerce_user_set",  # unique related_name
        related_query_name="ecommerce_user",
    )

    # Override the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="ecommerce_user_set",  # unique related_name
        related_query_name="ecommerce_user",
    )

# class User(AbstractUser):
#     department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)