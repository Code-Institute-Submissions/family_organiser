from django.test import TestCase
from .models import *
from user.functions.functions import create_test_user, get_users_profile

class TestModels(TestCase):

    def test_comment_method_returns_comment(self):
        user = create_test_user('1')
        users_profile = get_users_profile(user.id)
        user_profile = get_users_profile(user.id)
        comment = Comment(
            comment = 'Test comment',
            author = user,
            author_profile = user_profile,
        )
        self.assertEqual(str(comment), comment.comment)

    def test_status_method_returns_title(self):
        user = create_test_user('1')
        user_profile = get_users_profile(user.id)
        status = Status(
            user = user,
            user_profile = user_profile,
            title = 'Test title',
            content = 'Test content',
        )
        self.assertEqual(str(status), status.title)
    
    def test_comment_notification_method_returns_status_title(self):
        user_one = create_test_user('1')
        user_two = create_test_user('2')
        user_profile = get_users_profile(user_one.id)
        status = Status(
            user = user_one,
            user_profile = user_profile,
            title = 'Test title',
            content = 'Test content',
        )
        comment_notification = CommentNotification(
            user = user_one,
            status = status,
            commenter = user_two,
        )
        self.assertEqual(str(comment_notification), comment_notification.status.title)

    def test_like_notification_method_returns_username(self):
        user_one = create_test_user('1')
        user_two = create_test_user('2')
        user_profile = get_users_profile(user_one.id)
        status = Status(
            user = user_one,
            user_profile = user_profile,
            title = 'Test title',
            content = 'Test content',
        )
        like_notification = LikeNotification(
            user = user_one,
            status = status,
            liker = user_two,
        )
        self.assertEqual(str(like_notification), like_notification.user.username)