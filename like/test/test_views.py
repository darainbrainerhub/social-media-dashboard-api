from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework import status

User = get_user_model()

class LikeCreateViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.post_id = 1

    def test_like_create(self):
        url = reverse('like-create', kwargs={'pk': self.post_id})
        data = {'action': 'like'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_like_update(self):
        url = reverse('like-create', kwargs={'pk': self.post_id})
        data = {'action': 'like'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        like_id = response.data['id']
        
        data['action'] = 'dislike'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_undo(self):
        url = reverse('like-create', kwargs={'pk': self.post_id})
        data = {'action': 'like'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        like_id = response.data['id']
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CommentCreateViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.post_id = 1

    def test_comment_create(self):
        url = reverse('comment-create', kwargs={'pk': self.post_id})
        data = {'comment': 'Test comment'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
