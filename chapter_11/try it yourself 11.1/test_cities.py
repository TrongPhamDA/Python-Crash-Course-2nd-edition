# Create a file called test_cities.py that tests the function you
# just wrote (remember that you need to import unittest and the
# function you want to test). Write a method called
# test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the
# correct string. Run test_cities.py, and make sure
# test_city_country() passes.

import unittest
from city_functions import format_city_country as fcc

class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = fcc('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()