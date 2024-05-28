from django.test import TestCase
from user.models import User

class UserModelTest(TestCase):
    def setUp(self):
        pass


    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)

    def test_create_superuser(self):
        user = User.objects.create_superuser(username='admin', password='adminpass')
        self.assertEqual(user.username, 'admin')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_admin)

    