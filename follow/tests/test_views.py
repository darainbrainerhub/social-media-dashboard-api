from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from follow.models import Follow

User = get_user_model()

class FollowToggleViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.client = APIClient()

    def test_follow_toggle(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(reverse('follow_toggle', kwargs={'user_id': self.user2.id}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follow.objects.filter(follower=self.user1, following=self.user2).count(), 1)

    def test_unfollow_toggle(self):
        Follow.objects.create(follower=self.user1, following=self.user2)
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(reverse('follow_toggle', kwargs={'user_id': self.user2.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Follow.objects.filter(follower=self.user1, following=self.user2).count(), 0)

    def test_follow_toggle_invalid_user(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(reverse('follow_toggle', kwargs={'user_id': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_follow_toggle_self(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(reverse('follow_toggle', kwargs={'user_id': self.user1.id}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class FollowerCountViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        Follow.objects.create(follower=self.user1, following=self.user2)
        self.client = APIClient()

    def test_follower_count(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse('follower_count'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['followers'], 0)
        self.assertEqual(response.data['following'], 1)
