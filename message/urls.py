from django.urls import path
from . import views

urlpatterns = [
    path('select_conversation/', views.select_conversation, name="select_conversation"),
    path('new_conversation/', views.new_conversation, name="new_conversation"),
    path('conversation/<pk>', views.conversation, name="conversation"),
]

