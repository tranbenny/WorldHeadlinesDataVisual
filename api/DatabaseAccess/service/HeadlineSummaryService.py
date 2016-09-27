from DatabaseAccess.dao.HeadlineSummaryDAO import HeadlineSummaryDAO

# imports for generating a sample api call
import random
from pymongo import MongoClient
from Config.DataSources import LOCAL_DB_URL

class HeadlineSummaryService:

    def __init__(self):
        self.dao = HeadlineSummaryDAO()

    def findByDate(self, date):
        return self.dao.findByDate(date)

    def getSampleData(self):
        result = {}
        client = MongoClient(LOCAL_DB_URL)
        db = client['country']
        countries = []
        cursor = db['countries'].find()
        for document in cursor:
            countries.append(document['country_name'])

        for i in range(50):
            country = countries[random.randrange(len(countries))]
            result[country] = random.randrange(100)

        return result
        # return self.dao.getSampleData()