import requests
import time

from HeadlineData.ApiKey import NYTIMES_KEY

# class that gets nytimes world news headlines information
# TODO: NEED TO FIX THE COUNTRY FINDING

class NyTimesHeadlineService:

    BASE_URL = 'https://api.nytimes.com/svc/topstories/v1/world.json?api-key='
    API_ENDPOINT = "%s%s" % (BASE_URL, NYTIMES_KEY)

    def __init__(self):
        self.date = time.strftime('%Y-%m-%d')
        self.data = self.__getTodayHeadlines__()


    def __getTodayHeadlines__(self):
        '''
        :return: list of nytimes headlines
        '''
        result = []
        response = requests.get(self.API_ENDPOINT).json()['results']
        for value in response:
            keywords = []
            try:
                keywords = value['adx_keywords']
            except KeyError as error:
                keywords = []

            information = {
                'title' : value['title'].replace("'",""),
                'countries' : [],
                'headline_date' : self.date,
                'published_date' : value['published_date'],
                'description' : keywords,
                'source' : "New York Times"
            }
            information['published_date'] = information['published_date'][:10]
            result.append(information)
        return result


    def getHeadlines(self):
        '''
        :return: object access for getting headlines data
        '''
        return self.data

    def getTodayDate(self):
        '''
        :return: string date of when headlines were gathered
        '''
        return self.date

