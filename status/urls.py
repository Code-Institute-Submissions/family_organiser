from django.urls import path
from . import views

urlpatterns = [
    path('news_feed/', views.news_feed, name='news_feed'),
    path('update_status/<operation>/<pk>', views.update_status, name='update_status'),
    path('like_status/<pk>', views.like_status, name='like_status'),
    path('add_comment/<pk>/<redirect_user>', views.add_comment, name='add_comment'),
    path('view_status/<pk>', views.view_status, name='view_status'),
]
