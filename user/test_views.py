from django.test import TestCase, Client
from django.contrib.auth.models import User
from .functions.functions import create_test_user

class TestViews(TestCase):

    def test_get_family_page_user_not_authenticated(self):
        user = create_test_user()
        response = self.client.get(f'/user/family/{user.id}')
        self.assertEqual(response.status_code, 302)

    def test_get_family_page_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get(f'/user/family/{self.user.id}')
        self.assertEqual(response.status_code, 200)

    def test_get_find_users_page_user_not_authenticated(self):
        response = self.client.get('/user/find_users/')
        self.assertEqual(response.status_code, 302)

    def test_get_find_users_page_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get('/user/find_users/')
        self.assertEqual(response.status_code, 200)

    def test_get_notifications_page_user_not_authenticated(self):
        response = self.client.get('/user/notifications/')
        self.assertEqual(response.status_code, 302)

    def test_get_notifications_page_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get('/user/notifications/')
        self.assertEqual(response.status_code, 200)

    def test_get_profile_page_user_not_authenticated(self):
        response = self.client.get('/user/profile/')
        self.assertEqual(response.status_code, 302)

    def test_get_profile_page_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get('/user/profile/')
        self.assertEqual(response.status_code, 200)

    def test_get_settings_page_user_not_authenticated(self):
        response = self.client.get('/user/settings/')
        self.assertEqual(response.status_code, 302)

    def test_get_view_user_profile_page_user_not_authenticated(self):
        user = create_test_user()
        response = self.client.get(f'/user/view_user_profile/{user.id}')
        self.assertEqual(response.status_code, 302)