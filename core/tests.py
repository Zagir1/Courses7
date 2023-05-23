from django.test import TestCase, Client
from django.urls import reverse
from core import models


# Create your tests here.

class BookTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.book = models.Book.objects.create(title="Котёнок по имени Гав", num_of_reviews=55,
                                               summary="Простая история о простом котёнке с простой кличкой")

    def test_list_data(self):
        response = self.client.get(reverse('core:book_list'))
        self.assertEqual(response.status_code, 200)

