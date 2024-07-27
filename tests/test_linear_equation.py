from unittest import TestCase
from linear_equations import *

class LinearEquationTestCase(TestCase):
    def test_is_valid_number_0_division(self):
        # Zero Division
        self.assertEqual(False, is_valid_number("1/0"), "Should return False.")

    def test_is_valid_number_invalid_number(self):
        # Invalid Number
        self.assertFalse(is_valid_number("afds"))

    def test_is_valid_number_invalid_fraction(self):
        # Invalid Fraction
        self.assertFalse(is_valid_number("1/a"))
        self.assertFalse(is_valid_number("ghgsa/5"))
    
    def test_is_valid_number_invalid_decimal(self):
        # Test Invalid decimal
        self.assertFalse(is_valid_number("1..5"))
    
    def test_is_valid_number_invalid_negative_number(self):

        # Test invalid negative number --5
        self.assertFalse(is_valid_number("--5"))