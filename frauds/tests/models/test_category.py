from django.test import TestCase

from frauds.models import Category


class CategoryTestCase(TestCase):
    def test_category_function(self):
        category = Category.objects.create(name="qwe",
                                           description="jsrfefbaeilfbaek")

        expected = "Категорія: qwe - jsrfefbaeilfbaek"

        actual = category.category_function

        self.assertEqual(expected, actual)
