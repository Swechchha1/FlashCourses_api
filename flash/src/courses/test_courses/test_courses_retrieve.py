"""
FlashCourses- Test cases for API endpoints for retrieve using get method- Institution and course endpoints
Created By: Swechchha Tiwari  4/19/2018
Modified Date:  4/20/2018
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

class APIretrieveStatusCodeInstCourse(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment for GET method for institution_retrieve & course_retrieve.
        """

        inst = Institution.objects.create(ipeds = '12', institution_name = 'UNH', location = 'Manchester NH' )
        course_tbl = Course.objects.create(course_title = 'test', course_id = '2', course_description = 'this is a test data')

        self.retrieve_method_endpoint_courses = [
            reverse('courses:courses_api:institution_retrieve', kwargs = {'unique_id': Institution.objects.first().unique_id}),
            reverse('courses:courses_api:course_retrieve', kwargs = {'unique_id': Course.objects.first().unique_id}),
        ]

    def test_courses_endpoint_retrieve_method(self):
        """
        Create a request to every endpoint in retrieve_method_endpoint_courses. Ensure returns a 200
        response status code
        """
        c = Client()

        for endpoint in self.retrieve_method_endpoint_courses:
            response = c.get(endpoint)
            self.assertEqual(response.status_code, 200)
