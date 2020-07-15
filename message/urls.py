from django.urls import path
from . import views

urlpatterns = [
    path('start_conversation/', views.start_conversation, name="start_conversation"),
]

