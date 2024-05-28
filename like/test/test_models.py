from django.test import TestCase
from django.contrib.auth import get_user_model
from post.models import Post
from like.models import Like, Comment

User = get_user_model()

class LikeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post')
        self.like = Like.objects.create(user=self.user, post=self.post, action='like')

    def test_like_creation(self):
        self.assertEqual(Like.objects.count(), 1)
        saved_like = Like.objects.get(id=self.like.id)
        self.assertEqual(saved_like.user, self.user)
        self.assertEqual(saved_like.post, self.post)
        self.assertEqual(saved_like.action, 'like')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post')
        self.comment = Comment.objects.create(user=self.user, post=self.post, comment='This is a test comment')

    def test_comment_creation(self):
        self.assertEqual(Comment.objects.count(), 1)
        saved_comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(saved_comment.user, self.user)
        self.assertEqual(saved_comment.post, self.post)
        self.assertEqual(saved_comment.comment, 'This is a test comment')
