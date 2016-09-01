import os
import unittest
from pymongo import MongoClient

class CountryListTest(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient('mongodb://localhost:8000')
        # self.countries = []


    def test_database_added_all_countries_from_csv(self):
        numCountries = 0 # number of countries
        with open('INSERT PATH TO countries.csv HERE', 'r') as csv:
            for row in csv:
                numCountries += 1
        csv.close()
        numCountriesInDb = self.client.country.countries.count()
        self.assertNotEqual(numCountries, 0)
        self.assertEqual(numCountries, numCountriesInDb)