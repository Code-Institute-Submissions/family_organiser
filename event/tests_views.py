from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Event

class TestViews(TestCase):

    # menu page
    def test_get_menu_page_user_not_authenticated(self):
        response = self.client.get('/event/menu/')
        self.assertEqual(response.status_code, 302)

    def test_get_menu_page_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get('/event/menu/')
        self.assertEqual(response.status_code, 200)
