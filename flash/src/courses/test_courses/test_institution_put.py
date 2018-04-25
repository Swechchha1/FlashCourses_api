"""
FlashCourses- Test cases for API endpoint to update institution
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

class APIputStatusCodeTestsInstitution(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment.
        """

        user = User.objects.create_user('Swechchha', 'swechchha@gmail.com', 'imppwdswe')

        inst = Institution.objects.create(ipeds = '123654' , institution_name = 'UNH', location = 'Manchester' )


    def test_inst_endpoint_put_method(self):
        """
        Create a request to endpoint for put method and Ensure returns a 200
        response status code
        """

        c = Client()
        inst = Institution.objects.first()
        data = {
            'unique_id': inst.unique_id,
            'ipeds': inst.ipeds,
            'institution_name': inst.institution_name,
            'location': 'Concord, NH',
        }

        self.assertEqual(inst.location, 'Manchester')
        response = self.client.put(reverse('courses:courses_api:institution_update', kwargs = {'unique_id': inst.unique_id}), data)
        inst = Institution.objects.first()
        self.assertEqual(inst.location, 'Concord, NH')
        self.assertEqual(response.status_code, 200)
