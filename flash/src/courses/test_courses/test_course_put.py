"""
FlashCourses- Test cases for API endpoint to update course
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

class APIputStatusCodeTestsCourse(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment.
        """

        course_tbl = Course.objects.create(course_title = 'test', course_id = '815', course_description = 'this is a test data')

    def test_course_endpoint_put_method(self):
        """
        Create a request to endpoint for put method and Ensure returns a 200
        response status code
        """

        c = Client()
        course_tbl = Course.objects.first()
        data = {
            'unique_id': course_tbl.unique_id,
            'course_title': course_tbl.course_title,
            'course_description': course_tbl.course_description,
            'course_id': '215'

        }

        self.assertEqual(course_tbl.course_id, '815')
        response = self.client.put(reverse('courses:courses_api:course_update', kwargs = {'unique_id': course_tbl.unique_id}), data)
        course_tbl = Course.objects.first()
        self.assertEqual(course_tbl.course_id, '215')
        self.assertEqual(response.status_code, 200)
