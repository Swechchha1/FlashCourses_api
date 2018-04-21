"""
FlashCourses- Test cases for API endpoint deck create
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

class APIStatusCodeDeckCreate(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment. Add endpoint to be tested
        """

        self.post_method_endpoints_deck =[
            reverse('flashcards:flashcards_api:deck_create')
        ]

    def test_deck_endpoint_post_method_with_valid_data(self):
        """
        Create a request to deck create endpoint in post_method_endpoints. Ensure returns a 201
        response status code
        """

        c = Client()
        valid_data = {
            "username": "Test",
            "email": "test@gmail.com",
            "password": "somepassword",
            "deck_description" :  "testdescription",
            "title" : "Web application"
        }

        for endpoint in self.post_method_endpoints_deck:
            response = c.post(endpoint, valid_data, format = 'json')
        self.assertEqual(response.status_code, 201)

    def test_deck_endpoint_post_method_with_invalid_data(self):
        """
        Create a request to deck create endpoint in post_method_endpoints. Ensure returns a 400 for invalid data
        response status code
        """

        c = Client()
        invalid_data = {
             "username": "Test",
             "email": "swe@gmail.com",
             "password": "guestpassword",
             "title" : ""
        }

        for endpoint in self.post_method_endpoints_deck:
            response = c.post(endpoint, invalid_data, format = 'json')

        self.assertEqual(response.status_code, 400)
