import requests
from apiKey import nytimes_key

# class that gets nytimes world news headlines information

class nyTimesHeadlines():

    def __init__(self):
        self.base_url = 'https://api.nytimes.com/svc/topstories/v1/world.json?api-key='
        self.key = nytimes_key
        self.data = {}
        self.getTodayHeadlines()

    # makes api call to nytimes to get world headlines information
    # TODO: create function to format dates for keys
    def getTodayHeadlines(self):
        self.data['date'] = []
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
                'country' : value['geo_facet'],
                'published_date' : value['published_date'],
                'keywords' : keywords
            }
            self.data['date'].append(information)

    def getData(self):
        return self.data
