import os
import unittest
from pymongo import MongoClient
from DatabaseAccess.dao.CountriesDAO import CountriesDAO

from Config.DataSources import LOCAL_DB_URL

class CountryListTest(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient(LOCAL_DB_URL)
        # self.countries = []

    # fill in path to countries.csv file before running tests
    def test_database_added_all_countries_from_csv(self):
        numCountries = 0 # number of countries
        with open('INSERT PATH TO countries.csv HERE', 'r') as csv:
            for row in csv:
                numCountries += 1
        csv.close()
        numCountriesInDb = self.client.country.countries.count()
        self.assertNotEqual(numCountries, 0)
        self.assertEqual(numCountries, numCountriesInDb)

    def test_each_country_has_only_one_name(self):
        dao = CountriesDAO()
        countries = dao.__loadAllCountries__()
        for country in countries:
            self.assertIsInstance(country['country_name'], str)