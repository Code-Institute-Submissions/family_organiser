from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, related_name="category_user", on_delete=models.CASCADE)
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category

class Item(models.Model):
    user = models.ForeignKey(User, related_name="item_user", on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, related_name="item_category", on_delete=models.CASCADE)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.item

class PurchasedItems(models.Model):
    user = models.ForeignKey(User, related_name="purchased_item_user", on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, related_name="purchase_item_category", on_delete=models.CASCADE)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.item

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name="favorite_item_user", on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, related_name="favorite_item_category", on_delete=models.CASCADE)