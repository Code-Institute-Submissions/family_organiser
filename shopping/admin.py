from django.contrib import admin
from .models import Category, Item, PurchasedItems, Favorite, Partner, PartnerRequest

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'item',
        'category'
    )

class PurchasedItemsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'item',
        'category'
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'category'
    )

class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'item',
        'quantity',
    )

class PartnerRequestAdmin(admin.ModelAdmin):
    display_list = (
        'from_user',
        'to_user',
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(PurchasedItems, PurchasedItemsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Partner)
admin.site.register(PartnerRequest, PartnerRequestAdmin)