from django.urls import path
from . import views

urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    path('invite/<event_pk>/<user_pk>/', views.invite, name='invite'),
]