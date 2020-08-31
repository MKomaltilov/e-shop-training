from django.test import TestCase
from .models import Item


class ItemModelTest(TestCase):
    def test_item_can_be_created_with_default_params(self):
        Item.objects.create(
            title='item one'
        )

        item = Item.objects.first()
        self.assertRegexpMatches(
            str(item.id),
            r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b')
        self.assertEqual(item.title, 'item one')
        self.assertEqual(item.description, '')
        self.assertEqual(float(item.price), 0.00)

    def test_item_can_be_created_with_assigned_params(self):
        Item.objects.create(
            title='item one',
            description='item one description',
            price=1.15,
        )

        item = Item.objects.first()
        self.assertRegexpMatches(
            str(item.id),
            r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b')
        self.assertEqual(item.title, 'item one')
        self.assertEqual(item.description, 'item one description')
        self.assertEqual(float(item.price), 1.15)


class CategoryModelTest(TestCase):
    def test_category_can_be_created(self):
        Category.objects.create(
            name='category one'
        )
