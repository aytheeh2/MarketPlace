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