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


class CRUDCardTest(TestCase):
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

    def test_Card_create(self):
        """
        Testing object create operaions for Card model.
        """
    
        self.assertIsInstance(self.card, Card)

    def test_Card_retrieve(self):
        """
        Testing object retrieve operaions for Card model.
        """
        self.assertEqual(self.card.front, 'card1')
        self.assertEqual(self.card.back, 'card2')

    def test_Card_update(self):
        """
        Testing object update operaions for Card model.
        """
        c= Card.objects.filter(front='card1').update(back='card1')
        self.card= Card.objects.get(id=self.card.id)
        self.assertEqual(self.card.back, 'card1')

    def test_Card_delete(self):
        """
        Testing object delete operaions for Card model.
        """
        Card.objects.filter(front='card1').delete()
        self.assertEqual(Card.objects.count(),0)

