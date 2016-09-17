'''
DAO Object handles layer to interact with mongo database
'''

from pymongo import MongoClient
from Config.DataSources import LOCAL_DB_URL
from Config.DataSources import HEADLINE_COLLECTION_NAME

class HeadlineDAO:

    DATABASE_URL = LOCAL_DB_URL

    def __init__(self):
        try:
            client = MongoClient(self.DATABASE_URL)
        except:
            raise ConnectionError("Error establishing connection to database, make sure mongodb instance is running and allows connections")
        self.db = client.headlines


    def save(self, headline, collectionName):
        '''
        :param headline:
        :param collectionName:
        :return:
        '''
        self.db[collectionName].insert_one(headline)


    def saveMultiple(self, headlines, collectionName):
        '''
        :param headlines: dictionary/list, key = source, value = list of article objects
        :param collectionName: name of db collection to add to
        '''
        if isinstance(headlines, dict):
            for source in headlines.keys():
                self.db[collectionName].insert_many(headlines[source])
        else:
            self.db[collectionName].insert_many(headlines)

    def findByDate(self, date):
        '''
        :param date: string date
        :return: cursor instance pointing to list of headline objects from specified date
        '''
        results = self.db[HEADLINE_COLLECTION_NAME].find({
            'headline_date' : date
        })
        return results

    def findByCountry(self, country):
        return None

    def find(self, headline):
        return None

    def __validate__(self, headline):
        return None

    def update(self, headline):
        return None

    def findAll(self, criteria):
        return None

    def delete(self, criteria):
        return None
