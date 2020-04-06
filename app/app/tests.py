from django.test import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """Test calc 2 numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_number(self):
        """Test calc 2 numbers are subtracetd together"""
        self.assertEqual(subtract(5, 11), 6)
