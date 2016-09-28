'''
database interface for interacting with local mongo db in accessing country data
'''

from pymongo import MongoClient
import nltk


class CountriesDAO:

    LOCAL_DB_URL = 'mongodb://localhost:8000'

    def __init__(self):
        self.client = MongoClient(self.LOCAL_DB_URL)
        self.db = self.client.country


    def locateCountry(self, text):
        '''
        :param text: string headline title or headline description
        :return: list of countries mentioned in input text
        '''
        countries = []
        if not isinstance(text, list):
            tokens = nltk.tokenize.word_tokenize(text)
            for i in range(len(tokens)):
                token = tokens[i]
                if token == 'North' or token == 'South':
                    # check North Korea/South Korea
                    if (tokens[i + 1] == 'Korea' or tokens[i + 1] == 'Korean') and i < len(tokens) - 1:
                        name = token[i] + " " + token[i + 1]
                        relatedCountries = self._checkCountryEquality_(name)
                        countries.extend(relatedCountries)
                else:
                    relatedCountries = self._checkCountryEquality_(token)
                    countries.extend(relatedCountries)
        return countries

    def _checkCountryEquality_(self, word):
        '''
        :param String word
        :return: list of country names that matched passed word
        '''
        matches = []
        cursor = self.db['countries'].find({
            'country_name' : word
        })
        if cursor.count() > 0:
            for result in cursor:
                matches.append(result['country_name'])

        cursor = self.db['countries'].find({
            'other_names' : word
        })
        if cursor.count() > 0:
            for result in cursor:
                matches.append(result['country_name'])

        return matches

    def update(self, query, field):
        '''
        :param query:
        :param field:
        :return:
        '''
        self.db['countries'].update(query, field)