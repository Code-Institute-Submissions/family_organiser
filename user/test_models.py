from django.test import TestCase
from .models import UserProfile, AcceptedFriendRequests, FriendRequests, Friend
from .functions.functions import get_users_profile, create_test_user

class TestModels(TestCase):

    def test_accepted_friend_requests_method_returns_username(self):
        from_user = create_test_user('1')
        to_user = create_test_user('2')
        accepted_friend_request = AcceptedFriendRequests(
            from_user = from_user,
            to_user = to_user,
        )
        self.assertEqual(str(accepted_friend_request), 'testUsername1')

    def test_friend_requests_method_returns_username(self):
        from_user = create_test_user('1')
        to_user = create_test_user('2')
        friend_requests = FriendRequests(
            from_user = from_user,
            to_user = to_user,
        )
        self.assertEqual(str(friend_requests), 'testUsername2')

    def test_friend_method_returns_username(self):
        current_user = create_test_user('1')
        friend = Friend(
            current_user = current_user,
        )
        self.assertEqual(str(friend), 'testUsername1')       

    def test_user_profile_method_returns_username(self):
        user = create_test_user('1')
        user_profile = UserProfile.objects.create(
            user = user,
            age = 22,
            bio = 'test bio',
        )
        self.assertEqual(str(user_profile), 'testUsername1')

    def test_friend_class_method_make_friends(self):
        user_one = create_test_user('1')
        user_two = create_test_user('2')

        Friend.make_friend(user_one, user_two)

        friend_list = Friend.objects.get(current_user=user_one)
        user_ones_only_friend = friend_list.users.all()[0]

        self.assertEqual(user_ones_only_friend.username, user_two.username)

    def test_friend_class_method_remove_friends(self):
        user_one = create_test_user('1')
        user_two = create_test_user('2')

        Friend.make_friend(user_one, user_two)
        Friend.remove_friend(user_one, user_two)

        friend_list = Friend.objects.get(current_user=user_one)
        user_ones_only_friend = friend_list.users.all()

        self.assertEqual(len(user_ones_only_friend), 0) 
