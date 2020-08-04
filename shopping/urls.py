from django.urls import path
from . import views

urlpatterns = [
    path('shopping_page', views.shopping_page, name="shopping_page"),
    path('insight/<filter>', views.insight, name="insight"),
    path('add_partner', views.add_partner, name="add_partner"),
    path('quick_item/<item>/<category>', views.quick_item, name="quick_item"),
    path('update_category/<operation>/<pk>', views.update_category, name="update_category"),
    path('create_request/<pk>', views.create_request, name="create_request"),
    path('update_partners/<operation>/<pk>/<request_id>', views.update_partners, name='update_partners'),
    path('edit_item_quantity/<operation>/<pk>', views.edit_item_quantity , name="edit_item_quantity"),
    path('edit_purchased_item/<operation>/<pk>', views.edit_purchased_item , name="edit_purchased_item"),
    path('shopping_intro', views.shopping_intro, name="shopping_intro"),
]