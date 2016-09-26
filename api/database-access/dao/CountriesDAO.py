'''


'''

from pymongo import MongoClient
import nltk
from Config.DataSources import LOCAL_DB_URL

class CountriesDAO:

    def __init__(self):
        self.client = MongoClient(LOCAL_DB_URL)
        self.db = self.client.country
        self.countries = self.__loadAllCountries__()

    def __loadAllCountries__(self):
        '''
        :return: list of countries
        '''
        results = []
        for country in self.db.countries.find():
            results.append(country)
        return results


    def locateCountry(self, text):
        '''
        :param text: string headline title or headline description
        :return: list of countries mentioned in input text
        '''
        countries = []
        if not isinstance(text, list):
            tokens = nltk.tokenize.word_tokenize(text)
            for token in tokens:
                relatedCountries = self._checkCountryEquality_(token)
                countries.extend(relatedCountries)
        return countries


    def _checkCountryEquality_(self, word):
        '''
        :param word:
        :return:
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



    def addNewFieldToCountry(self, query, field):
        '''
        :param query:
        :param field:
        :return:
        '''
        self.db['countries'].update(query, field)



