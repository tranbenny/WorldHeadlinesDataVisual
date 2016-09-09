'''
TODO: NEED TO MAKE A BETTER COUNTRY MATCHING METHOD (Create a NLP service)

'''
from pymongo import MongoClient
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
        tokens = text.split(' ')
        relatedCountries = [self.__checkCountryEquality__(x) for x in tokens]
        return relatedCountries

    def __checkCountryEquality__(self, word):
        if (word.lower() in self.countries):
            return word.lower()
        elif (word.lower() == 'american' or word.lower() == 'america' or word.lower() == 'u.s.'):
            return "united states"
        else:
            result = self.__wordSimilarity__(word)
            if (result != False):
                return result

    def __wordSimilarity__(self, word):
        if (len(word) < 4):
            return False
        else:
            beginning = word[:4].lower()
            length = len(word)
            threshold = int(length * 0.6)
            filteredCountries = [x for x in self.countries if x['country_name'].startswith(beginning)]
            for value in filteredCountries:
                if value.startswith(word[:threshold].lower()):
                    return value.lower()
            return False
