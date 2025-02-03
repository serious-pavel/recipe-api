"""
Simple tests
"""

from django.test import SimpleTestCase

from . import calc


class ClassTests(SimpleTestCase):
    """Test the calc module"""

    def test_add(self):
        """Test adding numbers together"""

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test subtracting numbers together"""

        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
