from django.test import TestCase


class TestUrl(TestCase):
    def test_cart_url(self):
        response=self.client.get('/cart1/')
        print(response)
        self.assertEqual(response.status_code,200)