from django.test import TestCase
from .models import UserProfile
from .functions.functions import get_users_profile, create_test_user

class TestModels(TestCase):

    def test_user_profile_method_returns_username(self):
        user = create_test_user()
        user_profile = get_users_profile(user.id)
        self.assertEqual(str(user_profile), 'testUsername')

