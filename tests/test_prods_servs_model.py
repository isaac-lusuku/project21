from django.test import TestCase
from prods_servs.models import Product, Service  # Import the Product and Service models
from businesses.models import Selling_Business, Service_Business, Business  # Import relevant models from businesses app


class ProductTest(TestCase):
    def setUp(self):
        # Create a Business instance for testing
        self.business = Business.objects.create(
            owner=None,
            name="Furniture Kampala",
            city="Kampala",
            contact=2567588894,
            email="benjamin@gmail.com"
        )

        # Create a Selling_Business instance associated with the Business
        self.seller = Selling_Business.objects.create(
            category="furniture",
            business_details=self.business  # Link the Selling_Business to the Business instance
        )

    def test_product_creation(self):
        # Create a Product instance for testing
        product = Product.objects.create(
            name="Tables",
            units=5,
            seller=self.seller,  # Assign the previously created seller instance
            price=100,
            description="This is the best wood",
        )

        # Assertions to check if the product was created correctly
        self.assertEqual(product.name, "Tables")
        self.assertEqual(product.units, 5)
        self.assertEqual(product.seller, self.seller)  # Check if the seller instance matches the one assigned
        self.assertEqual(product.price, 100)
        self.assertEqual(product.description, "This is the best wood")


class ServiceTest(TestCase):
    def setUp(self):
        # Create a Business instance for testing
        self.business = Business.objects.create(
            owner=None,
            name="Furniture Kamapala",
            city="Kampala",
            contact=2567538894,
            email="benjmain@gmail.com"
        )

        # Create a Service_Business instance associated with the Business
        self.provider = Service_Business.objects.create(
            category='furniture',
            business_details=self.business  # Link the Service_Business to the Business instance
        )

    def test_service_creation(self):
        # Create a Service instance for testing
        service = Service.objects.create(
            service_name="furnishing",
            provider=self.provider,  # Assign the previously created provider instance
            price=200,
            description="we make your furniture adorable",
        )

        # Assertions to check if the service was created correctly
        self.assertEqual(service.service_name, "furnishing")
        self.assertEqual(service.provider, self.provider)  # Check if the provider instance matches the one assigned
        self.assertEqual(service.price, 200)
        self.assertEqual(service.description, "we make your furniture adorable")
