"""
Pritha Dutta
04.23.2018
Testing CRUD operations for models
"""

from django.test import TestCase
from datetime import date
import time
import random
from courses.models import Institution, Course
from flashcards.models import Deck, Card
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
import uuid


class CRUDUserTest(TestCase):
    institution = None;
    course = None;
    deck = None
    card = None;
    user = None;

    def setUp(self):
        """
        setUp needed to perform the tests, it is called before every test function.
        """
        self.institution = Institution.objects.create(institution_name='test_name', location='test_location')
        self.institution1 = Institution.objects.create(institution_name='test_name1', location='test_location1')
        self.course = Course.objects.create(course_id= 'test_id', course_title= 'title_123', course_description= 'description')
        self.course1 = Course.objects.create(course_id= 'test_id1', course_title = 'title_12', course_description= 'description1')
        self.deck = Deck.objects.create(title='deck1', deck_description= 'desc')
        self.card = Card.objects.create(front='card1', back='card2')
        self.user = User.objects.create(first_name = 'first_name', last_name = 'last_name', password='password')


    def test_User_create(self):
        """
        Testing object create operations for models
        """
        self.assertIsInstance(self.user, User)


    def test_User_retrieve(self):
        """
        Testing object retrieve operations for models
        """
        self.assertEqual(self.user.first_name, 'first_name')
        self.assertEqual(self.user.last_name, 'last_name')
        self.assertEqual(self.user.password, 'password')

    def test_User_update(self):
        """
        Testing object update operations for models
        """
        u = User.objects.filter(first_name='first_name').update(last_name='last_name1')
        self.user= User.objects.get(id=self.user.id)
        self.assertEqual(self.user.last_name, 'last_name1')

    def test_user_delete(self):
        """
        Testing object delete operations for models
        """
        User.objects.filter(first_name='first_name').delete()
        self.assertEqual(User.objects.count(),0)

