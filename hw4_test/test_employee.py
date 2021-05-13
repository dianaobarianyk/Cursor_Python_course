import unittest
from employee import Employee
from unittest.mock import Mock, patch


class TestForEmployee(unittest.TestCase):

    def setUp(self):
        self.classTest = Employee('Diana', 'Obarianyk', 10)

    def test_email(self):
        self.assertEqual(self.classTest.email, 'Diana.Obarianyk@email.com')

    def test_fullname(self):
        self.assertEqual(self.classTest.fullname, 'Diana Obarianyk')

    def test_apply_raise(self):
        self.classTest.apply_raise()
        self.assertEqual(self.classTest.pay, 10)

    @patch('requests.get')
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        response = self.classTest.monthly_schedule('January')
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
