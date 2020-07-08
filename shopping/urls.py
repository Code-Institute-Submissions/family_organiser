from django.urls import path
from . import views

urlpatterns = [
    path('shopping_page', views.shopping_page, name="shopping_page"),
]