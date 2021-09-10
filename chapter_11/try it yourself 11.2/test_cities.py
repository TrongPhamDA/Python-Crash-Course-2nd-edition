

import unittest
from city_functions import format_city_country as fcc

class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        # formatted_name = fcc('santiago', 'chile')
        formatted_name = fcc('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_name = fcc('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - 5000000')

if __name__ == '__main__':
    unittest.main()