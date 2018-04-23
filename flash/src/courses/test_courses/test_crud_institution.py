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


class CRUDInstitutionTest(TestCase):
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


    def test_Institution_create(self):
        """
        Testing object create operaions for Institution model.
        """
        self.assertIsInstance(self.institution, Institution)
        self.assertIsInstance(self.institution1, Institution)

    def test_Institution_retrieve(self):

        """
        Testing object retrieve operaions for Institution model.
        """
        self.assertEqual(self.institution.institution_name, 'test_name')
        self.assertEqual(self.institution.location, 'test_location')

    def test_Institution_update(self):
        """
        Testing object update operaions for Institution model.
        """
        c= Institution.objects.filter(institution_name='test_name1').update(location='test_loc')
        self.assertEqual(c, 1)
        self.institution1 = Institution.objects.get(id=self.institution1.id)
        self.assertEqual(self.institution1.location, 'test_loc')

    def test_institution_delete(self):
        """
        Testing object delete operaions for Institution model.
        """
        Institution.objects.filter(institution_name='test_name').delete()
        self.assertEqual(Institution.objects.count(),1)


