from django.db import models
from django.conf import settings 
from django.utils.translation import gettext_lazy as _
 

class Order(models.Model):
 
    # Order Status Choices
    class OrderStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        SHIPPED = 'SHIPPED', _('Shipped')
        DELIVERED = 'DELIVERED', _('Delivered')
        CANCELLED = 'CANCELLED', _('Cancelled')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='orders',
        verbose_name=_('User')
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_placed = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date Placed')
    )
    total_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name=_('Total Price')
    )
    is_successful = models.BooleanField(
        default=False,
        verbose_name=_('Is Successful')
    )
    status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name=_('Status')
    )
    objects = models.Manager()
    # Additional fields like shipping address can be added here

    def __str__(self):
        user_instance = self.user  # Fetch the related User instance
        return f"Order {self.pk} - {user_instance.username}"

    class Meta:
        ordering = ['-date_placed']
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
