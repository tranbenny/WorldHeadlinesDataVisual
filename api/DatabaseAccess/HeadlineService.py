'''
Headline Service to interact with data
'''

from DatabaseAccess.HeadlineDAO import HeadlineDAO

class HeadlineService:

    def __init__(self):
        self.headlineDao = HeadlineDAO()

    def find(self, criteria):
        return self.headlineDao.find(criteria)

    def findAll(self, criteria):
        return self.headlineDao.findAll(criteria)

    def findByDate(self, date):
        return self.findByDate(date)

    def findByCountry(self, country):
        return self.findByCountry(country)

    def save(self, headline, collectionName):
        self.headlineDao.save(headline, collectionName)

    def saveMultiple(self, headline, collectionName):
        self.headlineDao.saveMultiple(headline, collectionName)

    def update(self, headline):
        return self.headlineDao.update(headline)

    def delete(self, headline):
        return self.headlineDao.delete(headline)