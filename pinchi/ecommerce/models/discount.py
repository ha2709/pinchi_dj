from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from ecommerce.models.category import Category


class Discount(models.Model):
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('Percentage Discount'),
        help_text=_('Discount percentage for the product category and user category.')
    )
    product_category = models.ForeignKey(
        Category,  # Replace 'Category' with the correct Category model
        on_delete=models.CASCADE,
        verbose_name=_('Product Category')
    )
    USER_CATEGORY_CHOICES = [
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    ]
    user_category = models.CharField(
        max_length=50,
        choices=USER_CATEGORY_CHOICES,
        verbose_name=_('User Category')
    )

    objects = models.Manager()

    def __str__(self):
        return f"{self.user_category} - {self.product_category} - {self.percentage}% Discount"