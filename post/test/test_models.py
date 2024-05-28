from django.test import TestCase
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post_content = "Test post content"
        self.post = Post.objects.create(author=self.user, content=self.post_content)

    def test_post_creation(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.content, self.post_content)

    def test_post_str_method(self):
        expected_string = f'Post by {self.user.username} at {self.post.created_at}'
        self.assertEqual(str(self.post), expected_string)
