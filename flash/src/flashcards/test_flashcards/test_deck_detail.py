"""
FlashCourses- Test cases for API endpoints for get and retrieve for card and deck endpoints
Created By: Swechchha Tiwari  4/21/2018
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
from accounts.models import UserProfile

class APIgetStatusCodeDeckdetail(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment for GET method for card_retrieve and deck_retrieve based on unique_id.
        """
        user = User.objects.create_user('Swechchha', 'swechchha@gmail.com', 'imppwdswe')
        user.save()
        course_tbl = Course.objects.create(course_title = 'test', course_id = '2', course_description = 'this is a test data')
        course_tbl.save()
        deck_tbl = Deck.objects.create(title = 'test title', deck_description = 'this is a test')
        deck_tbl.save()
        card_tbl = Card.objects.create(front = 'test', back = 'testsback')
        card_tbl.save()

        self.detail_method_endpoint = [
            reverse('flashcards:flashcards_api:deck_detail', kwargs = {'unique_id': Deck.objects.first().unique_id}),
        ]

    def test_deck_endpoint_detail_method(self):
        """
        Create a request to every endpoint in retrieve_method_endpoints. Ensure returns a 200
        response status code
        """
        c = Client()

        for endpoint in self.detail_method_endpoint:
            response = c.get(endpoint)
        self.assertEqual(response.status_code, 200)
