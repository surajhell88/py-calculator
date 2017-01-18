import unittest
from unittest import TestCase
from calculator import addition, negation

class TestAddition(TestCase):
    def test_addition(self):
        a = 6
        b = 9
        result = addition(a, b)
        self.assertEqual(15, result)

    def test_negation(self):
        a = 9
        b = 6
        result = negation(a, b)
        self.assertEqual(3, result)

suite = unittest.TestLoader().loadTestsFromTestCase(TestAddition)
unittest.TextTestRunner().run(suite)