from django.contrib import admin
from .models import Category, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)