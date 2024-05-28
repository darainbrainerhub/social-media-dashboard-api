from django.test import TestCase
from django.contrib.auth import get_user_model
from follow.models import Follow

User = get_user_model()

class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

    def test_follow_creation(self):
        follow = Follow.objects.create(follower=self.user1, following=self.user2)
        self.assertEqual(follow.follower, self.user1)
        self.assertEqual(follow.following, self.user2)
        self.assertIsNotNone(follow.created_at)

    def test_unique_follow_constraint(self):
        # Attempt to create a duplicate follow relationship
        Follow.objects.create(follower=self.user1, following=self.user2)
        # Attempt to create the same follow relationship again
        with self.assertRaises(Exception):
            Follow.objects.create(follower=self.user1, following=self.user2)

    def test_follow_str_representation(self):
        follow = Follow.objects.create(follower=self.user1, following=self.user2)
        self.assertEqual(str(follow), f'{self.user1.username} follows {self.user2.username}')
