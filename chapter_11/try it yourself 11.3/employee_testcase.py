# try it yourself 11.3

import unittest
from employee import Employee

class TestCase(unittest.TestCase):
    def setUp(self):
        self.employee0 = Employee('Trong', 'Pham', 8870)
    def test_raise_default(self):
        self.employee0.give_raise()
        self.assertEqual(self.employee0.annual_salary, 13870)
    def test_raise_other(self):
        self.employee0.give_raise(500)
        self.assertEqual(self.employee0.annual_salary, 9370)

if __name__ == '__main__':
    unittest.main()