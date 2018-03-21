import unittest
from app.calculator import Calculator

class TddInPythonAttempt(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_add_method_returns_correct_results(self):
        result = self.calc.add(10,2)
        self.assertEqual(12, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
