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

class APIStatusCodeInstCreate(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment. Add endpoint to be tested
        """

        self.post_method_endpoint_institution =[
            reverse('courses:courses_api:institution_create')
        ]

    def test_course_endpoint_post_method_with_valid_data(self):
        """
        Create a request to institution create endpoint in post_method_endpoint_institution. Ensure returns a 201
        response status code
        """

        c = Client()

        """
        All the three fields in valid_data are mandatory fields for creating data
        """

        valid_data = {
            "ipeds": "ws",
            "institution_name": "UNH",
            "location" : "Manchester"
        }

        for endpoint in self.post_method_endpoint_institution:
            response = c.post(endpoint, valid_data, format = 'json')
        self.assertEqual(response.status_code, 201)

    def test_course_endpoint_post_method_with_invalid_data(self):
        """
        Create a request to institution create endpoint in post_method_endpoint_institution. Ensure returns a 400 for invalid data
        response status code
        """

        c = Client()
        invalid_data = {
             "ipeds": "",
             "institution_name": "UNH",
             "location" : "Manchester"

        }

        for endpoint in self.post_method_endpoint_institution:
            response = c.post(endpoint, invalid_data, format = 'json')

        self.assertEqual(response.status_code, 400)
