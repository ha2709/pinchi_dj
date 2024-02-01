from django.db import models
from django.conf import settings
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
    def get_order_count(self):
        # Assuming an Order model with a ForeignKey to User and an is_successful field
        return self.order_set.filter(is_successful=True).count()

    def get_customer_category(self):
        order_count = self.get_order_count()
        if order_count <= settings.CUSTOMER_CATEGORIES['BRONZE']:
            return 'Bronze'
        elif order_count <= settings.CUSTOMER_CATEGORIES['SILVER']:
            return 'Silver'
        else:
            return 'Gold'