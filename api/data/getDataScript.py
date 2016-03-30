from bs4 import BeautifulSoup
import apiKey
import requests
import pickle
import re

countryList = pickle.load(open('countries.py', 'rb'))
countryList = [x.lower() for x in countryList]

rssFeeds1 = apiKey.rssFeeds1
rssFeeds2 = apiKey.rssFeeds2
urls = rssFeeds1 + rssFeeds2

# takes in string title and article description, returns list of all countries mentioned
def findCountry(title, description):
    tokens1 = title.split(' ')
    relatedCountries1 = [x for x in tokens1 if x.lower() in countryList]
    tokens2 = description.split(' ')
    relatedCountries2 = [x for x in tokens2 if x.lower() in countryList]
    combinedList = relatedCountries1 + relatedCountries2
    return set(combinedList)


def getData(url):
    data = []
    text = requests.get(url).text
    soup = BeautifulSoup(text, 'html.parser')

    container = soup.find_all('item')
    # attributes: <title>, <pubdate>, <description>
    for result in container:
        article = {}
        title = result.find('title').text
        description = result.find('description').text
        if url in rssFeeds1:
            title = str(title)
            description = str(description)
        else:
            title = str(title.encode('utf8'))
            description = str(description.encode('utf8'))
        description = re.sub('<[^>]*>', '', description)  # gets rid of internal tags
        article['title'] = title
        article['description'] = description
        article['date'] = str(result.find('pubdate').text)
        article['countries'] = list(findCountry(title, description))
        data.append(article)
    return data


def getAllData():
    result = {}
    for url in urls:
        print('started ' + url)
        result[url] = getData(url)
        print("finished " + url )
    # create script to use nyTimesHeadlines Object here



if __name__ == "__main__":
    # run code here
    getAllData()