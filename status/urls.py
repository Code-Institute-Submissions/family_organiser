from django.urls import path
from . import views

urlpatterns = [
    path('news_feed/', views.news_feed, name='news_feed'),
    path('add_status/', views.add_status, name='add_status'),
    path('like_status/<pk>', views.like_status, name='like_status'),
]
