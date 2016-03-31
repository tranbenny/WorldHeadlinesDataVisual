from bs4 import BeautifulSoup
from monthMapping import months
import nyTimesHeadlines
import apiKey
import requests
import pickle
import re
import time
import databaseConfig as db

try:
    import mysql.connector
except:
    print("make sure mysql-connector-python is installed, install from mysql site")


# loads data from nytimes api and various rss feeds
# formats data to be loaded into database
# adds data to database

'''
TODO:
- FOR FINDING COUNTRIES, NEED TO FORMAT A WAY FOR ADJECTIVES TO BE FOUND
- NYTIMES:
    - find country, DONE
    - add format time function, DONE
- RSS FEEDS:
    - add format time function, DONE
- CREATE A FORMAT THAT CAN BE TURNED INTO SQL STATEMENT: needs to be a list of objects
'''

currentDate = time.strftime('%Y-%m-%d')

countryList = pickle.load(open('countries.py', 'rb'))
countryList = [x.lower() for x in countryList]

rssFeeds1 = apiKey.rssFeeds1
rssFeeds2 = apiKey.rssFeeds2
urls = rssFeeds1 + rssFeeds2

# takes in string title and article description, returns list of all countries mentioned
def findCountry(title, description):
    tokens1 = title.split(' ')
    relatedCountries1 = [checkWordCountry(x) for x in tokens1]
    tokens2 = description
    if (type(description) == type('exampleString')):
        tokens2 = description.split(' ')
    relatedCountries2 = [checkWordCountry(x) for x in tokens2]
    combinedList = relatedCountries1 + relatedCountries2
    combinedList = [word for word in combinedList if word != None]
    return set(combinedList)

# takes a string and returns a country if word matches or is close
def checkWordCountry(word):
    if (word.lower() in countryList):
        return word.lower()
    elif (word.lower() == "american"):
        return "united states"
    else:
        # use a string match threshold
        result = wordSimilarity(word)
        if result != False:
            return result


# find the closest looking word in list
# list is alphabetical
def wordSimilarity(word):
    if (len(word) < 4):
        return False
    else:
        beginning = word[:4].lower()
        length = len(word)
        threshold = int(length * (0.6))
        # find matching country with first 4 letters
        filteredCountries = [x for x in countryList if x.startswith(beginning)]
        # if more than 60% of the characters match, return the country
        for value in filteredCountries:
            if value.startswith(word[:threshold].lower()):
                return value
        return False





# takes in published date string and formats into date string for database
def formatRSSDate(date):
    result = ""
    tokens = date.split(" ")
    result = tokens[3] + "-" + months[tokens[2]] + "-" + tokens[1]
    return result



# gets data from nytimes object
# currentDate: formatted date string of day that api call was made
# headlines: list of all article data
def getNyTimesData():
    nyTimes = nyTimesHeadlines.nyTimesHeadlines()
    headlines = nyTimes.getData()
    for item in headlines:
         item['country'] = list(findCountry(item['title'], item['description']))
    return headlines

# gets data from all RSS feed URLs
def getRSSData(url):
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
        article['published_date'] = str(result.find('pubdate').text)
        article['published_date'] = formatRSSDate(article['published_date'])
        article['countries'] = list(findCountry(title, description))
        article['source'] = apiKey.sourcesMapping[url]
        data.append(article)
    return data

# gets all the scraped data from all the rss feeds
def getAllData():
    result = {}
    for url in urls:
        print('started ' + url)
        result[apiKey.sourcesMapping[url]] = getRSSData(url)
        print("finished " + url)
        print(result[apiKey.sourcesMapping[url]][0])
    return result

# connects to database
def createDatabaseConnection():
    cnx = mysql.connector.connect(user=db.user, password=db.password, host=db.host, database=db.database)



if __name__ == "__main__":
    nyTimesData = getNyTimesData()
    rssData = getAllData()





