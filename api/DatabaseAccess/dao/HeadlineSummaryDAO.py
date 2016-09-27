from pymongo import MongoClient
from Config.DataSources import LOCAL_DB_URL, HEADLINE_SUMMARY_COLLECTION_NAME


class HeadlineSummaryDAO:

    def __init__(self):
        self.collection = 'country_count' # change for production
        client = MongoClient(LOCAL_DB_URL)
        self.db = client[HEADLINE_SUMMARY_COLLECTION_NAME] # country_count

    def findByDate(self, date):
        '''
        :param date: string date value
        :return: dict object, key = countries, value = # of articles from country
        '''
        query = {
            'date': date
        }
        # cursor object
        cursor = self.db[self.collection].find(query)
        result = cursor.next()
        return result['count']

    def __findAll__(self, date):
        '''
        :param date: string date value
        :return: cursor object for summary daya results
        only used for testing
        '''
        query = {'date' : date }
        return self.db[self.collection].find(query)


    def saveSummaryData(self):
        return None
