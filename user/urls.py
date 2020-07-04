from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('find_users/', views.find_users, name='friends'),
]
