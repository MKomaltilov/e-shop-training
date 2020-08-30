from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):
    def test_product_can_be_created_with_default_params(self):
        Product.objects.create(
            title='product one'
        )

        product = Product.objects.first()
        self.assertRegexpMatches(
            str(product.id),
            r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b')
        self.assertEqual(product.title, 'product one')
        self.assertEqual(product.description, '')
        self.assertEqual(float(product.price), 0.00)

    def test_product_can_be_created_with_assigned_params(self):
        Product.objects.create(
            title='product one',
            description='product one description',
            price=1.15,
        )

        product = Product.objects.first()
        self.assertRegexpMatches(
            str(product.id),
            r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b')
        self.assertEqual(product.title, 'product one')
        self.assertEqual(product.description, 'product one description')
        self.assertEqual(float(product.price), 1.15)
