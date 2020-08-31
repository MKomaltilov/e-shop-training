from django.db import IntegrityError
from django.test import TestCase
from .models import Item, Category


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

    def test_item_can_be_assigned_to_few_categories(self):
        category_one = Category.objects.create(name='category one')
        category_two = Category.objects.create(name='category two')
        category_three = Category.objects.create(name='category three')

        item = Item.objects.create(title='item one')
        item.categories.add(category_one)
        item.categories.add(category_three)
        item.save()

        expected_item = Item.objects.first()
        categories = expected_item.categories.all()

        self.assertEqual(len(categories), 2)
        self.assertIn(category_one, categories)
        self.assertIn(category_three, categories)

        self.assertNotIn(category_two, categories)


class CategoryModelTest(TestCase):
    def test_category_can_be_created(self):
        Category.objects.create(
            name='category one'
        )

        category = Category.objects.first()
        self.assertRegexpMatches(
            str(category.id),
            r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b')
        self.assertEqual(category.name, 'category one')

    def test_category_name_should_be_unique(self):
        Category.objects.create(
            name='category one'
        )
        with self.assertRaises(IntegrityError):
            category = Category.objects.create(
                name='category one'
            )
            category.full_clean()
            categories = Category.objects.all()
            self.assertEqual(len(categories), 1)
