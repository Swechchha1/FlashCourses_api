"""
FlashCourses- Test cases for API endpoints
Created By: Swechchha Tiwari  4/6/2018
Modified Date:  4/17/2018
"""

import json
import uuid

from django.shortcuts import reverse
from django.test import Client, TestCase
from .. models import Deck, Card
from courses.models import Institution, Course
from django.contrib.auth.models import User
#from accounts.models import User
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
        self.valid_data = {
            "username": "Test",
            "email": "test@gmail.com",
            "password": "somepassword",
            "course_title" : "testing",
            "course_id" : "11",
            "course_description": "web application",
            "title" : "Web Application",
            "deck_description" :  "testdescription"
                     }

        user = User.objects.create_user('Swechchha', 'swechchha@gmail.com', 'imppwdswe')
        user.save()
        course_tbl = Course.objects.create(course_title = 'test', course_id = '2', course_description = 'this is a test data')
        course_tbl.save()
        deck_tbl = Deck.objects.create(title = 'rofl', deck_description = 'testing')
        deck_tbl.save()
        card_tbl = Card.objects.create(front = 'test', back = 'testback')
        card_tbl.save()

        self.deck_endpoint_put_method = [
                reverse('flashcards:flashcards_api:deck_update', kwargs = {'unique_id': Card.objects.first().unique_id}),
            ]


    def test_deck_endpoint_put_method(self):
        """
        Create a request to every endpoint in put_method_endpoints. Ensure returns a 200/204
        response status code
        """

        c = Client()
        #print('*************************')
        #print(self.deck_endpoint_put_method)
        #print(type(self.deck_endpoint_put_method))
        #print('*************************')

        for endpoint in self.deck_endpoint_put_method:
            #print('###############################')
            #print(endpoint)
            #response = c.put(endpoint, data = json.dumps(self.valid_data), format = 'json')
            response = c.put(endpoint, {'title' : 'testdata'})
            #print(response)
        self.assertEqual(response.status_code, 200)
