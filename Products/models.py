from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='Category_images', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Category'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='Item_images', blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} : {self.category}"


class Offers(models.Model):
    offer_item = models.ForeignKey(
        Item, related_name='offers', on_delete=models.CASCADE)
    offer_date_added = models.DateTimeField(auto_now_add=True)
    offer_starts = models.DateTimeField(auto_now=True)
    offer_ends = models.DateTimeField(auto_now=True)
    discount_rate = models.FloatField()

    @property
    def offer_discount(self):
        item_price = self.offer_item.price
        return round(item_price * self.discount_rate)

    class Meta:
        verbose_name_plural = "Offers"

    def __str__(self):
        return f"{self.offer_item.name} : {self.offer_item.category}"
