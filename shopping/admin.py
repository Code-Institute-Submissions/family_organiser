from django.contrib import admin
from .models import Category, Item, PurchasedItems, Favorite

# Register your models here.
admin.site.register(Item)
admin.site.register(PurchasedItems)
admin.site.register(Category)
admin.site.register(Favorite)