from django.test import TestCase, Client
from .models import PartnerRequest
from .functions.functions import *
from user.functions.functions import create_test_user

class TestFunctions(TestCase):

    def test_get_partner_request_returns_empty_list(self):
        self.client = Client()
        self.user = create_test_user('1')
        self.client.login(username='testUsername1', password='Password777')
        shopping_partners = get_partner_requests(self)
        self.assertEqual(len(shopping_partners), 0)

    def test_get_shopping_partners_returns_a_list(self):
        self.client = Client()
        self.user = create_test_user('1')
        partner = create_test_user('2')
        self.client.login(username='testUsername1', password='Password777')

        partner_request = PartnerRequest(
            from_user = partner,
            to_user = self.user,
        )
        partner_request.save()

        shopping_partners = get_partner_requests(self)
        self.assertEqual(len(shopping_partners), 1)