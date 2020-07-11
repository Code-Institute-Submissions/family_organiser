from django.urls import path
from . import views

urlpatterns = [
    path('shopping_page', views.shopping_page, name="shopping_page"),
    path('insight', views.insight, name="insight"),
    path('add_partner', views.add_partner, name="add_partner"),
    path('update_item/<operation>', views.update_item, name="update_item"),
    path('quick_item/<item>/<category>', views.quick_item, name="quick_item"),
    path('update_category/<operation>/<pk>', views.update_category, name="update_category"),
    path('create_request/<pk>', views.create_request, name="create_request"),
    path('update_partners/<operation>/<pk>/<request_id>', views.update_partners, name='update_partners'),
]