from django.test import TestCase
from django.contrib.auth import get_user_model
from main_info.models import UserProfile

# Get the custom user model
User = get_user_model()

# Test class for custom user model
class MyUserModelTest(TestCase):

    # Test creating a regular user
    def test_create_user(self):
        user = User.objects.create_user(
            email='benjamin@gmail.com',
            username='benjamin',
            password='benpassword'
        )
        # Assertions for user attributes
        self.assertEqual(user.email, 'benjamin@gmail.com')
        self.assertEqual(user.username, 'benjamin')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # Test creating a user with missing required fields
    def test_create_user_with_missing_fields(self):
        # Test missing email
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', username='benajmin', password='benpassword')
        # Test missing username
        with self.assertRaises(ValueError):
            User.objects.create_user(email='benjamin@gmail.com', username='', password='benpassword')
        # Test missing password
        with self.assertRaises(ValueError):
            User.objects.create_user(email='benjamin@gmail.com', username='benajamin', password='')

    # Test creating a superuser
    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email='admin@django.com',
            username='adminuser',
            password='adminpassword'
        )
        # Assertions for superuser attributes
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    # Test creating a superuser with missing required fields
    def test_create_superuser_with_missing_fields(self):
        # Test missing email
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='', username='adminuser', password='adminpassword')
        # Test missing username
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='admin@django.com', username='', password='adminpassword')
        # Test missing password
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='admin@django.com', username='adminuser', password='')

# Test class for UserProfile model
class UserProfileModelTest(TestCase):

    # Set up method to create a user for testing UserProfile
    def setUp(self):
        user = User.objects.create_user(
            email='benjamin@gmail.com',
            username='benajmin',
            password='benpassword'
        )
        self.user = user

    # Test creating a user profile with required fields
    def test_create_user_profile(self):
        profile = UserProfile.objects.create(
            user=self.user,
            phone=2563988894,
            bio='I like online shopping'
        )
        # Assertions for user profile attributes
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.phone, 2563988894)
        self.assertEqual(profile.bio, 'I like online shopping')
        self.assertTrue(profile.is_active)
        self.assertIsNotNone(profile.date_joined)

    # Test creating a user profile with optional fields
    def test_create_user_profile_with_optional_fields(self):
        profile = UserProfile.objects.create(
            user=self.user,
            bio='I like online shopping'
        )
        # Assertion for optional field 'phone'
        self.assertIsNone(profile.phone)
