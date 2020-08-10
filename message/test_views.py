from django.test import TestCase, Client
from django.contrib.auth.models import User
from user.functions.functions import create_test_user

# Create your tests here.
class TestViews(TestCase):

    def test_get_conversation_user_not_authenticated(self):
        user = create_test_user()
        message_user = User.objects.create_user('test', 'test@test.com', 'Password777')
        response = self.client.get(f'/message/conversation/{message_user.id}')
        self.assertEqual(response.status_code, 302)
