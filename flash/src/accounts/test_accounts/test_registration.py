"""
FlashCourses- Test cases for API registration endpoint
Created By: Swechchha Tiwari  4/6/2018
Modified Date:  4/16/2018
"""

import json

from django.shortcuts import reverse
from django.test import Client, TestCase
from flashcards.models import Deck, Card
from courses.models import Institution, Course
from django.contrib.auth.models import User
from rest_framework import status

class RegisterationTestCases(TestCase):
    def setUp(self):
        """
        create a user and add endpoint for registration
        """

        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

        self.create_url = reverse('accounts:accounts_api:reg_api')

    def test_reg_endpoint_post_with_valid_data(self):
        """
        Ensure we can create a new user and that we're returning a 201 http status code.
        """
        data = {
            'username': 'Test',
            'email': 'test@gmail.com',
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url , data)

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 201)

    def test_reg_endpoint_post_with_invalid_data(self):
        """
        Ensure we can cannot create a new user with inavlid data and that we're returning a 400 error code.
        """
        invalid_user_data = {
            'username': '',
            'email': 'swechchhagmail.com',
            'password': ''
        }

        response = self.client.post(self.create_url , invalid_user_data)

        self.assertEqual(response.status_code, 400)
