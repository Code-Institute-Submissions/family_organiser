from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('create_event/', views.create_event, name='create_event'),
    path('invite/<event_pk>/<user_pk>/', views.invite, name='invite'),
    path('event/<pk>/', views.event, name='event'),
    path('remove_event/<pk>/', views.remove_event, name='remove_event'),
]