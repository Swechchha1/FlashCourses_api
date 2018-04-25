"""
FlashCourses- Test cases for API Login authentication endpoint
Created By: Swechchha Tiwari  4/21/2018
Modified Date:  4/23/2018
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

class LoginTestAuthentication(TestCase):
    def setUp(self):
        """
        Creating test_user for authentication and endpoints for token_obtain_pair, token_refresh and token_verify
        """

        self.endpoint_obtain_token = reverse('token_obtain_pair')
        self.endpoint_refresh_token = reverse('token_refresh')
        self.endpoint_verify_token = reverse('token_verify')

        self.test_user = User.objects.create_user('test1', 'test@test.com', 'tqwe123qwe')

        self.credentials = {

            'username': 'test1',
            'password': 'tqwe123qwe',

             }

        self.invalid_credentials = {

            'username': 'test_user',
            'password': 'qwe123qw',

            }

        self.requests = Client()

    def test_obtain_token_success(self):
        """
        Obtaining token if user is authenticated successfully with response status 200
        """

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(self.endpoint_obtain_token, self.credentials)
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
        response = self.requests.post(self.endpoint_obtain_token, self.invalid_credentials)
        self.assertEqual(response.status_code, 400)
        return response

    def test_refresh_token_success(self):
        """
        Check if token refresh is successfull then response status is 200
        """
        refresh = RefreshToken()

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(self.endpoint_refresh_token, data = {'refresh':str(refresh)})
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
        response = self.requests.post(self.endpoint_refresh_token, data = {})
        self.assertEqual(response.status_code, 400)
        return response

    def test_verify_token_success(self):
        """
        Check if token verified successfully then response status is 200
        """

        token = AccessToken()

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(self.endpoint_verify_token, data = {'token':str(token)})
        self.assertEqual(response.status_code, 200)
        #print("***************")
        #print(response.content)
        #print("***************")
        return response

    def test_verify_token_failure(self):
        """
        Check if token verification is not successfull then response status is 400
        """

        token = AccessToken()

        self.assertEqual(User.objects.count(), 1)
        response = self.requests.post(self.endpoint_verify_token, data = {})
        self.assertEqual(response.status_code, 400)
        return response
