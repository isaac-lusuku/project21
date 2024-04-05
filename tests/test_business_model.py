from django.test import TestCase
from main_info.models import MyUser
from businesses.models import Business, Selling_Business, Service_Business
import datetime

# Test class for Business model
class BusinessModelTest(TestCase):

    # Set up method to create a user for testing foreign key relationships
    def setUp(self):
        self.user = MyUser.objects.create_user(
            email='benjamin@gmail.com',
            username='benjamin',
            password='benpassword'
        )

    # Test creating a basic Business instance
    def test_create_business(self):

        # Create a Business instance
        business = Business.objects.create(
            owner=self.user,
            name='Kampala Furniture',
            city='Kampala',
            contact=2563988894,
        )
        # Assertions for Business attributes
        self.assertEqual(business.owner, self.user)
        self.assertEqual(business.name, 'Kampala Furniture')
        self.assertEqual(business.city, 'Kampala')
        self.assertEqual(business.contact, 2563988894)
        self.assertIsNone(business.email)  # Email is blank
        
    # Test creating a Business instance with optional fields
    def test_create_business_with_optional_fields(self):

        # Create a Business instance with optional fields
        business = Business.objects.create(
            name='Kampala Furniture',
            city='Furniture',
            contact=2563988894,
            email='benjamin@gmail.com',
            # logo will be tested in a separate test (if applicable)
        )
        # Assertion for optional field 'email'
        self.assertEqual(business.email, 'benjamin@gmail.com')

    # Test creating a Selling_Business instance
    def test_create_selling_business(self):
        # Create a Business instance
        business = Business.objects.create(
            owner=self.user,
            name='Furniture Kampala',
            city='Kampala',
            contact=2563988894,
        )
        # Create a Selling_Business instance
        selling_business = Selling_Business.objects.create(
            business_details=business,
            category='Furniture',
            delivery_options=True,
        )
        # Assertions for Selling_Business attributes
        self.assertEqual(selling_business.business_details, business)
        self.assertEqual(selling_business.category, 'Furniture')
        self.assertTrue(selling_business.delivery_options)

    # Test creating a Service_Business instance
    def test_create_service_business(self):
        # Create a Business instance
        business = Business.objects.create(
            owner=self.user,
            name='Furniture Kampala',
            city='Kampala',
            contact=2563988894,
        )
        # Create a Service_Business instance
        service_business = Service_Business.objects.create(
            business_details=business,
            category='Furnishing',
            appointment_options=True,
        )
        # Assertions for Service_Business attributes
        self.assertEqual(service_business.business_details, business)
        self.assertEqual(service_business.category, 'Furnishing')
        self.assertTrue(service_business.appointment_options)
