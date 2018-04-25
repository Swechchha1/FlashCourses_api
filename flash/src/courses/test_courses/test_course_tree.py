"""
FlashCourses- Test cases for API endpoints for course tree endpoint
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

class APIgetStatusCourseTree(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment for GET method for course_tree based on unique_id.
        """
        user = User.objects.create_user('Swechchha', 'swechchha@gmail.com', 'imppwdswe')
        inst = Institution.objects.create(ipeds = '123654' , institution_name = 'UNH', location = 'Manchester' )
        course_tbl = Course.objects.create(course_title = 'test', course_id = '2', course_description = 'this is a test data')
        deck_tbl = Deck.objects.create(title = 'test title', deck_description = 'this is a test')
        card_tbl = Card.objects.create(front = 'test', back = 'testsback')

        self.endpoint_course_tree = [
            reverse('courses:courses_api:course_tree', kwargs = {'unique_id': Course.objects.first().unique_id}),
        ]

    def test_course_endpoint_tree(self):
        """
        Create a request to endpoint in endpoint_course_tree Ensure returns a 200
        response status code
        """
        c = Client()

        for endpoint in self.endpoint_course_tree :
            response = c.get(endpoint)
        self.assertEqual(response.status_code, 200)
