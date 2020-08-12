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
        self.assertEqual(str(category), 'test')

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
        self.assertEqual(str(item), 'testItem')

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
        self.assertEqual(str(purchased_item), 'testItem')
        
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
        self.assertEqual(str(favourite), 'testItem')



