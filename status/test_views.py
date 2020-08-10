from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Status
from user.functions.functions import create_test_user, get_users_profile
from .functions.functions import create_test_status

class TestViews(TestCase):

    def test_get_news_feed_page_user_not_authenticated(self):
        response = self.client.get('/status/news_feed/')
        self.assertEqual(response.status_code, 302)

    def test_get_news_feed_page_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get('/status/news_feed/')
        self.assertEqual(response.status_code, 200)

    def test_get_view_status_page_user_not_authenticated(self):
        status = create_test_status()
        response = self.client.get(f'/status/view_status/{status.id}')
        self.assertEqual(response.status_code, 302)

    def test_get_view_status_page_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        user_profile = get_users_profile(self.user.id)
        status = create_test_status()
        response = self.client.get(f'/status/view_status/{status.id}')
        self.assertEqual(response.status_code, 200) 