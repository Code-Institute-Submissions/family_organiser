from django.test import TestCase, Client
from .models import User
from .functions.functions import create_test_user

class TestViews(TestCase):

    def test_get_family_page_user_not_authenticated(self):
        user = create_test_user()
        response = self.client.get(f'/user/family/{user.id}')
        self.assertEqual(response.status_code, 302)

    # def test_get_find_users_page(self):

    # def test_get_notifications_page(self):

    # def test_get_profile_page(self):

    # def test_get_settings_page(self):

    # def test_get_view_user_profile_page(self):