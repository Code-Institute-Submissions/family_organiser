from django.test import TestCase, Client
from django.contrib.auth.models import User
from user.functions.functions import create_test_user

# Create your tests here.
class TestViews(TestCase):

    # Conversation page
    def test_get_conversation_user_not_authenticated(self):
        user = create_test_user('1')
        message_user = User.objects.create_user('test', 'test@test.com', 'Password777')
        response = self.client.get(f'/message/conversation/{message_user.id}')
        self.assertEqual(response.status_code, 302)

    def test_get_conversation_user_authenticated(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
        message_user = User.objects.create_user('test2', 'test2@test.com', 'Password777')
        self.client.login(username='test', password='Password777')
        response = self.client.get(f'/message/conversation/{message_user.id}')
        self.assertEqual(response.status_code, 200)

    # New conversation page
    # def test_get_new_conversation_user_not_authenticated(self):
    #     user = create_test_user()
    #     response = self.client.get('/message/new_conversation')
    #     self.assertEqual(response.status_code, 302)

    # def test_get_new_conversation_user_authenticated(self):
    #     self.client = Client()
    #     self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
    #     self.client.login(username='test', password='Password777')
    #     response = self.client.get('/message/new_conversation')
    #     self.assertEqual(response.status_code, 200)

    # Select Conversation page
    # def test_get_select_conversation_page_not_authenticated(self):
    #     user = create_test_user()
    #     message_user = User.objects.create_user('test', 'test@test.com', 'Password777')
    #     response = self.client.get('/message/select_conversation')
    #     self.assertEqual(response.status_code, 302)

    # def test_get_select_conversation_page_authenticated(self):
    #     self.client = Client()
    #     self.user = User.objects.create_user('test', 'test@test.com', 'Password777')
    #     message_user = User.objects.create_user('test2', 'test2@test.com', 'Password777')
    #     self.client.login(username='test', password='Password777')
    #     response = self.client.get('/message/select_conversation')
    #     self.assertEqual(response.status_code, 200)