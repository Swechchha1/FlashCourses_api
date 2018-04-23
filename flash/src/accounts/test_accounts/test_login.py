"""
FlashCourses- Test cases for API authentication endpoint
Created By: Swechchha Tiwari  4/21/2018
Modified Date:  4/22/2018
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

test_user = {
    'username': 'test1',
    'email': 'test@test.com',
    'password': 'qwe123qwe',
    }

credentials = {

    'username': 'test1',
    'password': 'qwe123qwe',

     }

invalid_credentials = {

    'username': 'test_user',
    'password': 'qwe123qw',

    }

endpoint_obtain_token = reverse('token_obtain_pair')
endpoint_refresh_token = reverse('token_refresh')
endpoint_verify_token = reverse('token_verify')

class TestAuthentication(TestCase):
    def setUp(self):
        """
        Creating test_user for authentication
        """

        User.objects.create_user(**test_user)
        self.requests = Client()

    def test_obtain_token_success(self):
        """
        Obtaining token if user is authenticated successfully with response status 200
        """

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(endpoint_obtain_token, credentials)
        self.assertEqual(response.status_code, 200)
        print("***************")
        print(response.content)
        print("***************")
        return response

    def test_obtain_token_failure(self):
        """
        If user is credentials are not valid then response status should be 400
        """

        user = User.objects.first()
        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(endpoint_obtain_token, invalid_credentials)
        self.assertEqual(response.status_code, 400)
        return response

    def test_refresh_token_success(self):
        """
        Check if token refresh is successfull then response status is 200
        """
        refresh = RefreshToken()

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(endpoint_refresh_token, data = {'refresh':str(refresh)})
        self.assertEqual(response.status_code, 200)
        print("***************")
        print(response.content)
        print("***************")
        return response

    def test_refresh_token_failure(self):
        """
        Check if token refresh is not successfull then response status is 400
        """

        refresh = RefreshToken()

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(endpoint_refresh_token, data = {})
        self.assertEqual(response.status_code, 400)
        return response

    def test_verify_token_success(self):
        """
        Check if token verified successfully then response status is 200
        """

        token = AccessToken()

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(endpoint_verify_token, data = {'token':str(token)})
        self.assertEqual(response.status_code, 200)
        print("***************")
        print(response.content)
        print("***************")
        return response

    def test_verify_token_failure(self):
        """
        Check if token verification is not successfull then response status is 400
        """

        token = AccessToken()

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(endpoint_verify_token, data = {})
        self.assertEqual(response.status_code, 400)
        return response
