import unittest
from DatabaseAccess.CountriesDAO import CountriesDAO

class CountriesDAOTest(unittest.TestCase):

    def setUp(self):
        self.dao = CountriesDAO()

    def test_reads_all_countries_from_db(self):
        countryList = self.dao.__loadAllCountries__()
        self.assertEqual(len(countryList), 268)
