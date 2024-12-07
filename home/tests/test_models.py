from django.test import TestCase
from home.models import Books

class TestModels(TestCase):
    def test_book_model(self):
        # Create a book instance
        book1 = Books.objects.create(name="wings", price=12, stock=15)

        # Assert string representation (update "wings" as per your model's __str__ method)
        self.assertEqual(str(book1), "wing")  # Update this based on your model's __str__ implementation

        # Assert the instance is of type Books
        self.assertTrue(isinstance(book1, Books))
