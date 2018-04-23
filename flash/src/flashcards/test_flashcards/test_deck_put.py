"""
FlashCourses- Test cases for API endpoints
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

class APIputStatusCodeTestsDeck(APITestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up testing environment. Add all endpoints to be tested
        """

        user = User.objects.create_user('Swechchha', 'swechchha@gmail.com', 'imppwdswe')
        user.save()
        course_tbl = Course.objects.create(course_title = 'test', course_id = '2', course_description = 'this is a test data')
        course_tbl.save()
        deck_tbl = Deck.objects.create(title = 'test title', deck_description = 'testing')
        deck_tbl.save()

    def test_deck_endpoint_put_method(self):
        """
        Create a request to every endpoint in put_method_endpoints. Ensure returns a 200
        response status code
        """

        c = Client()
        deck = Deck.objects.first()
        data = {
            "unique_id": deck.unique_id,
            "parent_user": deck.parent_user.id,
            "parent_course": deck.parent_course.id,
            "title": "some new title",
            "deck_description": deck.deck_description
        }

        self.assertEqual(deck.title, "test title")
        response = self.client.put(reverse('flashcards:flashcards_api:deck_update', kwargs = {'unique_id': deck.unique_id}), data)
        deck = Deck.objects.first()
        self.assertEqual(deck.title, 'some new title')
        self.assertEqual(response.status_code, 200)
