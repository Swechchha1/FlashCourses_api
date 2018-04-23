"""
FlashCourses- Test cases for API endpoints for deleting data in institution
Created By: Swechchha Tiwari  4/22/2018
Modified Date:
"""

import json
import uuid

from django.shortcuts import reverse
from django.test import Client, TestCase
from flashcards.models import Deck, Card
from courses.models import Institution, Course
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

class APIdeleteStatusCodeTestsInst(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment. Add all endpoints to be tested
        """

        inst = Institution.objects.create(ipeds = '12', institution_name = 'UNH', location = 'Manchester NH' )

        self.delete_method_endpoint_institution = [
            reverse('courses:courses_api:institution_delete', kwargs = {'unique_id': Institution.objects.first().unique_id}),

        ]

    def test_self_delete_method_endpointsdeck(self):
        """
        Create a request to every endpoint in delete_method_endpoints. Ensure returns a 204
        response status code
        """
        c = Client()

        for endpoint in self.delete_method_endpoint_institution:
            response = c.delete(endpoint)
        self.assertEqual(response.status_code, 204)
        #self.assertEqual(User.objects.count(), 0)
