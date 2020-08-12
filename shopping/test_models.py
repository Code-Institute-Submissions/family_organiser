from django.test import TestCase
from .models import *
from user.functions.functions import create_test_user

class TestModels(TestCase):

    def test_category_method_returns_category(self):
        user = create_test_user('1')
        category = Category(
            user = user,
            category = 'test',
        )
        self.assertEqual(str(category), category.category)

    def test_item_method_returns_item(self):
        user = create_test_user('1')
        category = Category(
            user = user,
            category = 'testCategory',
        )
        item = Item(
            user = user,
            item = 'testItem',
            category = category,
        )
        self.assertEqual(str(item), item.item)

    def test_purchased_items_method_returns_item(self):
        user = create_test_user('1')
        category = Category(
            user = user,
            category = 'testCategory',
        )
        purchased_item = PurchasedItems(
            user = user,
            item = 'testItem',
            category = category,
        )
        self.assertEqual(str(purchased_item), purchased_item.item)
        
    def test_favorite_method_returns_item(self):
        user = create_test_user('1')
        category = Category(
            user = user,
            category = 'testCategory',
        )
        favourite = Favorite(
            user = user,
            item = 'testItem',
            category = category,
        )
        self.assertEqual(str(favourite), favourite.item)

    def test_partner_request_method_returns_username(self):
        user_one = create_test_user('1')
        user_two = create_test_user('2')
        partner_request = PartnerRequest(
            from_user = user_one,
            to_user = user_two,
        )
        self.assertEqual(str(partner_request), user_one.username)

    def test_partner_method_returns_username(self):
        user = create_test_user('1')
        partner = Partner(
            current_user = user,
        )
        self.assertEqual(str(partner), user.username)




