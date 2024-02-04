# models.py
from django.db import models
from ecommerce.models.product import Product

class ShoppingCart(models.Model):
    products = models.ManyToManyField(Product)
    objects = models.Manager()
