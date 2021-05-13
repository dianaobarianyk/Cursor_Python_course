import unittest
from functions_to_test import Calculator


class TestForCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(5, 7), 12)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 3), 7)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(4, 7), 28)

    def test_divide(self):
        self.assertEqual(Calculator.divide(12, 6), 2)
        with self.assertRaises(ValueError):
            Calculator.divide(12, 0)


if __name__ == '__main__':
    unittest.main()
