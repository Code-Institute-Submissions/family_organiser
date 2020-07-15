from django.urls import path
from . import views

urlpatterns = [
    path('premium_info/', views.premium_info, name='premium_info'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('payment_successful/', views.payment_successful, name='payment_successful'),
]
