"""
FlashCourses- Test cases for API endpoints for deleting data in deck
Created By: Swechchha Tiwari  4/13/2018
Modified Date:  4/22/2018
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

class APIdeleteStatusCodeDeck(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment. Add all endpoints to be tested
        """
        userone = User.objects.create_user('Swechchha', 'swechchha@gmail.com', 'imppwdswe')
        userone.save()
        course_tbl = Course.objects.create(course_title = 'test', course_id = '2', course_description = 'this is a test data')
        course_tbl.save()
        deck_tbl = Deck.objects.create(title = 'testone', deck_description = 'testdescription')
        deck_tbl.save()

        self.delete_method_endpoints_deck = [
            reverse('flashcards:flashcards_api:deck_delete', kwargs = {'unique_id': Deck.objects.first().unique_id}),

        ]

    def test_self_delete_method_endpointsdeck(self):
        """
        Create a request to every endpoint in delete_method_endpoints. Ensure returns a 204
        response status code
        """
        c = Client()

        deck = Deck.objects.first()
        for endpoint in self.delete_method_endpoints_deck:
            response = c.delete(endpoint)
        self.assertEqual(response.status_code, 204)
        #self.assertEqual(User.objects.count(), 0)
