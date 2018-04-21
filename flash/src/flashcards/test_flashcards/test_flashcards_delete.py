"""
FlashCourses- Test cases for API endpoints for deleting data
Created By: Swechchha Tiwari  4/6/2018
Modified Date:  4/17/2018
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

class APIStatusCodeTests(APITestCase):

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
        card_tbl = Card.objects.create(front = 'test', back = 'testone')
        card_tbl.save()

        usertwo = User.objects.create_user('Swech', 'swecha@gmail.com', 'impperrwe')
        usertwo.save()
        course_tbltwo = Course.objects.create(course_title = 'testdata', course_id = '3', course_description = 'this is test')
        course_tbltwo.save()
        deck_tbltwo = Deck.objects.create(title = 'testtwo', deck_description = 'test')
        deck_tbltwo.save()
        card_tbltwo = Card.objects.create(front = 'testing', back = 'testtwo')
        card_tbltwo.save()

        self.delete_method_endpoints_deck = [
            reverse('flashcards:flashcards_api:deck_delete', kwargs = {'unique_id': Deck.objects.first().unique_id}),

        ]

        self.delete_method_endpoints_card = [
            reverse('flashcards:flashcards_api:card_delete', kwargs = {'unique_id': Card.objects.first().unique_id}),

        ]

    def test_self_delete_method_endpointsdeck(self):
        """
        Create a request to every endpoint in delete_method_endpoints. Ensure returns a 204
        response status code
        """
        c = Client()

        for endpoint in self.delete_method_endpoints_deck:
            response = c.delete(endpoint,)
        self.assertEqual(response.status_code, 204)
        #self.assertEqual(User.objects.count(), 1)

    def test_self_delete_method_endpointscard(self):
        """
        Create a request to every endpoint in delete_method_endpoints. Ensure returns a 204
        response status code
        """
        c = Client()

        for endpoint in self.delete_method_endpoints_card:
            response = c.delete(endpoint)
        self.assertEqual(response.status_code, 204)
        #self.assertEqual(User.objects.count(), 1)
