import uuid
from django.db import models
from django.contrib.auth.models import User
from Products.models import Category, Item, Offers
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(
        User, related_name='cart_user', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    products = models.ForeignKey(
        Item, related_name='cart_products', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.products.name

    def subtotal(self):
        return self.quantity * self.products.price


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name='order_user', on_delete=models.CASCADE,)
    delivery_status = models.CharField(default="Pending", max_length=10)
    order_status = models.CharField(default="Pending", max_length=10)
    ordered_date = models.DateTimeField(auto_now_add=True)
    Products = models.ForeignKey(Item, on_delete=models.CASCADE)
    no_of_items_ordered = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.order_id}:{self.user}:{self.Products.name}'
