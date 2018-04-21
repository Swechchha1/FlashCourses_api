"""
FlashCourses- Test cases for API endpoints for get- card and deck endpoints
Created By: Swechchha Tiwari  4/6/2018
Modified Date:  4/17/2018
"""

import json
import uuid

from django.shortcuts import reverse
from django.test import Client, TestCase
from flashcards.models import Deck, Card
from courses.models import Institution, Course
from accounts.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import UserProfile

class APIgetStatusCodeDeckCard(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment for GET method for deck_list & card_list.
        """

        self.get_method_endpoints = [
            reverse('flashcards:flashcards_api:deck_list'),
            reverse('flashcards:flashcards_api:card_list'),

        ]

    def test_flashcards_endpoint_get_method(self):
        """
        Crate a request to every endpoint in get_method_endpoints. Ensure returns a 200
        response status code
        """

        c = Client()

        for endpoint in self.get_method_endpoints:
            response = c.get(endpoint)
            self.assertEqual(response.status_code, 200)
