import requests
from apiKey import nytimes_key
import time

# class that gets nytimes world news headlines information
# TODO: NEED TO FIX THE COUNTRY FINDING

class nyTimesHeadlines():

    def __init__(self):
        self.base_url = 'https://api.nytimes.com/svc/topstories/v1/world.json?api-key='
        self.key = nytimes_key
        self.date = time.strftime('%Y-%m-%d')
        self.data = []
        self.getTodayHeadlines()

    # makes api call to nytimes to get world headlines information
    def getTodayHeadlines(self):
        api_endpoint = self.base_url + self.key
        response = requests.get(api_endpoint).json()['results']
        for value in response:
            keywords = []
            try:
                keywords = value['adx_keywords']
            except KeyError as error:
                keywords = []

            information = {
                'title' : value['title'],
                'countries' : [],
                'published_date' : value['published_date'],
                'description' : keywords,
                'source' : "New York Times"
            }
            information['published_date'] = information['published_date'][:10]
            self.data.append(information)

    # returns a list of artile objects
    def getData(self):
        return self.data

    # returns date that api call was made
    def getTodayDate(self):
        return self.date

