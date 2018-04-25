"""
FlashCourses- Test cases for API endpoints for get and retrieve for card and deck endpoints
Created By: Swechchha Tiwari  4/22/2018
Modified Date:
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

class APIgetStatusInstitutiondetail(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment for GET method for card_retrieve and deck_retrieve based on unique_id.
        """

        inst = Institution.objects.create(ipeds = '123654' , institution_name = 'UNH', location = 'Manchester' )
        course_tbl = Course.objects.create(course_title = 'test', course_id = '2', course_description = 'this is a test data')


        self.detail_method_endpoint_institution = [
            reverse('courses:courses_api:institution_detail', kwargs = {'unique_id': Institution.objects.first().unique_id}),
        ]

    def test_detail_method_endpoint_inst(self):
        """
        Create a request to every endpoint in retrieve_method_endpoints. Ensure returns a 200
        response status code
        """
        c = Client()

        for endpoint in self.detail_method_endpoint_institution:
            response = c.get(endpoint)
        self.assertEqual(response.status_code, 200)
