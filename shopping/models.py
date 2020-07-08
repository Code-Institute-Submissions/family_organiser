from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, related_name="category_user", on_delete=models.CASCADE)
    category = models.CharField(max_length=150)

class Item(models.Model):
    user = models.ForeignKey(User, related_name="item_user", on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, related_name="item_category", on_delete=models.CASCADE)