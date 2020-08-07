from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, related_name="category_user", on_delete=models.CASCADE)
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category

class Item(models.Model):
    user = models.ForeignKey(User, related_name="item_user", on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, related_name="item_category", on_delete=models.CASCADE)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.item

class PurchasedItems(models.Model):
    user = models.ForeignKey(User, related_name="purchased_item_user", on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, related_name="purchase_item_category", on_delete=models.CASCADE)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.item

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name="favorite_item_user", on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, related_name="favorite_item_category", on_delete=models.CASCADE)

    @classmethod
    def add_or_update_favourite(cls, item_name, category, request):
        try:
            favorite = Favorite.objects.get(item=item_name, user=request.user)
            favorite.quantity += 1
            favorite.save()
        except:
            favorite_item = Favorite(
                user = request.user,
                item = item_name,
                quantity = 1,
                category = category, 
            )
            favorite_item.save()

    def __str__(self):
        return self.item

class PartnerRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="partner_fromuser", null=True, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.from_user.username

class Partner(models.Model):
    partners = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name="partner_owner", null=True, on_delete=models.CASCADE)

    @classmethod
    def make_partner(cls, current_user, new_friend):
        partner, created = cls.objects.get_or_create(
            current_user=current_user
        )
        partner.partners.add(new_friend)

    @classmethod
    def remove_partner(cls, current_user, new_friend):
        partner, created = cls.objects.get_or_create(
            current_user=current_user
        )
        partner.partners.remove(new_friend)

    def __str__(self):
        return self.current_user.username