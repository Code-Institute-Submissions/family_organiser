from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('find_users/', views.find_users, name='find_users'),
    path('create_request/<pk>', views.create_friend_request, name='friends'),
    path('update_friends/<operation>/<pk>/<request_id>', views.update_friends, name='update_friends'),
    path('requests/', views.requests, name='requests'),
    path('family/', views.family, name='family'),
    path('settings/', views.settings, name='settings'),
    path('change_image/', views.change_profile_image, name='change_image'),
    path('change_details/', views.change_profile_details, name='change_details'),
]
