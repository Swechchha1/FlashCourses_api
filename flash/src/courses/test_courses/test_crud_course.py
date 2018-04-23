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


class CRUDCourseTest(TestCase):
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

    def test_Course_create(self):
        """
        Testing object create operaions for Course model.
        """
        self.assertIsInstance(self.course, Course)
        self.assertIsInstance(self.course1, Course)

    def test_Course_retrieve(self):
        """
        Testing object retrieve operaions for Course model.
        """
        self.assertEqual(self.course.course_id, 'test_id')
        self.assertEqual(self.course.course_title, 'title_123')
        self.assertEqual(self.course.course_description, 'description')
        self.assertEqual(self.course1.course_id, 'test_id1')
        self.assertEqual(self.course1.course_title, 'title_12')
        self.assertEqual(self.course1.course_description, 'description1')

    def test_Course_update(self):
        """
        Testing object update operaions for Course model.
        """
        
        b = Course.objects.filter(course_title= 'title_123').update(course_id='test_id2')
        self.assertEqual(b, 1)
        self.course = Course.objects.get(id=self.course.id)
        self.assertEqual(self.course.course_id, 'test_id2')

    def test_course_delete(self):
        """
        Testing object delete operations for Course model
        """
        Course.objects.filter(course_title = 'title_123').delete()
        self.assertEqual(Course.objects.count(),1)


