from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class TestViews(TestCase):

    # family page
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)