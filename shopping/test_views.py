from django.test import TestCase, Client
from django.contrib.auth.models import User
from user.functions.functions import create_test_user, get_users_profile
from .models import Category

class TestViews(TestCase):

    # insight page
    def test_get_insight_page_user_not_authenticated(self):
        user = create_test_user()
        response = self.client.get('/shopping/insight/personal')
        self.assertEqual(response.status_code, 302)

    def test_get_insight_page_user_authenticated_not_premium(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get('/shopping/insight/personal')
        self.assertEqual(response.status_code, 302)

    def test_get_insight_page_user_authenticated_premium(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        user_profile = get_users_profile(self.user.id)
        user_profile.premium = True
        user_profile.save()
        response = self.client.get('/shopping/insight/personal')
        self.assertEqual(response.status_code, 200)

    # shopping intro page
    def test_get_shopping_intro_page_user_not_authenticated(self):
        user = create_test_user()
        response = self.client.get('/shopping/shopping_intro')
        self.assertEqual(response.status_code, 302)

    def test_get_shopping_intro_page_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        user_profile = get_users_profile(self.user.id)
        user_profile.premium = True
        user_profile.save()
        response = self.client.get('/shopping/shopping_intro')
        self.assertEqual(response.status_code, 200)

    # Shopping page
    def test_get_shopping_page_user_not_authenticated(self):
        user = create_test_user()
        response = self.client.get('/shopping/shopping_page')
        self.assertEqual(response.status_code, 302)

    def test_get_shopping_page_user_authenticated_no_categories(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get('/shopping/shopping_page')
        self.assertEqual(response.status_code, 302)

    def test_get_shopping_page_user_authenticated_with_categories(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        new_category = Category(
            user = self.user,
            category = 'testCategory',
        )
        new_category.save()
        response = self.client.get('/shopping/shopping_page')
        self.assertEqual(response.status_code, 200)

    # Shopping partner page
    def test_get_shopping_partner_page_user_not_authenticated(self):
        user = create_test_user()
        response = self.client.get('/shopping/add_partner')
        self.assertEqual(response.status_code, 302)

    def test_get_shopping_partner_page_user_authenticated_not_premium(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get('/shopping/add_partner')
        self.assertEqual(response.status_code, 302)

    def test_get_shopping_partner_page_user_authenticated_premium(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        user_profile = get_users_profile(self.user.id)
        user_profile.premium = True
        user_profile.save()
        response = self.client.get('/shopping/add_partner')
        self.assertEqual(response.status_code, 200)

