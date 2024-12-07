from django.test import TestCase
from django.urls import resolve,reverse
from home.models import Books

class testView(TestCase):
    def test_home_view(self):
        client=client()
        response=client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')