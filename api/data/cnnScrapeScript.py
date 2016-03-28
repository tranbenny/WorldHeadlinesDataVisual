from bs4 import BeautifulSoup
from apiKey import cnnRSSUrl
import requests
import pickle
import re

# TODO: need to load results into database

# create list of all countries
countryList = pickle.load(open('countries.py', 'rb'))
countryList = [x.lower() for x in countryList]


# takes in string title and article description, returns list of all countries mentioned
def findCountry(title, description):
    tokens1 = title.split(' ')
    relatedCountries1 = [x for x in tokens1 if x.lower() in countryList]
    tokens2 = description.split(' ')
    relatedCountries2 = [x for x in tokens2 if x.lower() in countryList]
    combinedList = relatedCountries1 + relatedCountries2
    return set(combinedList)


# CNN
def getDataFromCNN():
    data = []
    text = requests.get(cnnRSSUrl).text
    soup = BeautifulSoup(text, 'html.parser')

    container = soup.find_all('item')
    # attributes: <title>, <pubdate>, <description>
    for result in container:
        article = {}
        title = str(result.find('title').text)
        article['title'] = title
        description = str(result.find('description').text)
        description = re.sub('<[^>]*>', '', description) # gets rid of internal tags
        article['description'] = description
        article['date'] = str(result.find('pubdate').text)
        article['countries'] = list(findCountry(title, description))
        data.append(article)
    # print(data)


if __name__ == '__main__':
    getDataFromCNN()











