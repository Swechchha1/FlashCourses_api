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


class CRUDDeckTest(TestCase):
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

    def test_Deck_create(self):
        """
        Testing object create operations for Deck model
        """
        self.assertIsInstance(self.deck, Deck)
    
    def test_Deck_retrieve(self):
        """
        Testing object retrieve operations for Deck model
        """
        self.assertEqual(self.deck.title, 'deck1')
        self.assertEqual(self.deck.deck_description, 'desc')

    def test_Deck_update(self):
        """
        Testing object update operations for Deck model
        """
        d= Deck.objects.filter(title='deck1').update(title='deck2')
        self.deck= Deck.objects.get(id=self.deck.id)
        self.assertEqual(self.deck.title, 'deck2')

    def test_deck_delete(self):
        """
        Testing object delete operations for Deck model
        """
        Deck.objects.filter(title='deck1').delete()
        self.assertEqual(Deck.objects.count(),0)

