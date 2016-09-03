from bs4 import BeautifulSoup
import nyTimesHeadlines
import apiKey
import requests
import pickle
import re
import time
import databaseConfig as db


# loads HeadlineData from nytimes api and various rss feeds
# formats HeadlineData to be loaded into database
# adds HeadlineData to database
# THIS SCRIPT SHOULD BE RUN ONCE A DAY


currentDate = time.strftime('%Y-%m-%d')

countryList = pickle.load(open('countries.py', 'rb'))
countryList = [x.lower() for x in countryList]

urls = apiKey.rssFeeds

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
    elif (word.lower() == "american" or word.lower() == "us" or word.lower() == "u.s."):
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
                return value.lower()
        return False





# takes in published date string and formats into date string for database
def formatRSSDate(date):
    result = ""
    tokens = date.split(" ")
    result = tokens[3] + "-" + months[tokens[2]] + "-" + tokens[1]
    return result



# gets HeadlineData from nytimes object
# currentDate: formatted date string of day that api call was made
# headlines: list of all article HeadlineData
def getNyTimesData():
    nyTimes = nyTimesHeadlines.nyTimesHeadlines()
    headlines = nyTimes.getData()
    for item in headlines:
         item['countries'] = list(findCountry(item['title'], item['description']))
    return headlines

# gets HeadlineData from all RSS feed URLs
def getRSSData(url):
    data = []
    text = requests.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    container = soup.find_all('item')
    # attributes: <title>, <pubdate>, <description>
    for result in container:
        article = {}
        title = result.find('title').text
        try:
            description = result.find('description').text
        except:
            description = ''

        try:
            title = getRidOfTags(str(title)).replace("'", "")
            description = getRidOfTags(str(description))
        except:
            title = getRidOfTags(str(title.encode('utf8')))
            # print(title)
            description = getRidOfTags(str(description.encode('utf8')))
            # print(description)
        description = re.sub('<[^>]*>', '', description)  # gets rid of internal tags
        article['title'] = title.replace("'", "")
        article['description'] = description.replace("'", "")
        try:
            article['published_date'] = str(result.find('pubdate').text)
            article['published_date'] = formatRSSDate(article['published_date'])
        except:
            article['published_date'] = currentDate
        article['countries'] = list(findCountry(title, description))
        article['source'] = apiKey.sourcesMapping[url]
        data.append(article)
    return data

# gets all the scraped HeadlineData from all the rss feeds
def getAllData():
    result = {}
    for url in urls:
        print('started ' + url)
        result[apiKey.sourcesMapping[url]] = getRSSData(url)
        print("finished " + url)
    return result

# connects to database
def createDatabaseConnection(nyData, rssData):
    # connect to database and execute statements
    print("starting to load into database")
    cnx = mysql.connector.connect(user=db.user, password=db.password, host=db.host, database=db.database)
    cursor = cnx.cursor(buffered=True)
    for value in nyData:
        sqlStatement = "INSERT INTO " + db.TABLE_NAME + " VALUES" + createSQLStatement(value) + ";"
        try:
            cursor.execute("FAILED INSERT: " + sqlStatement)
        except:
            print(sqlStatement)
            continue
    sources = rssData.keys()
    for source in sources:
        articles = rssData[source] # list
        for article in articles:
            sqlStatement = "INSERT INTO " + db.TABLE_NAME + " VALUES " + createSQLStatement(article) + ";"
            try:
                cursor.execute(sqlStatement)
            except:
                print("FAILED INSERT: " + sqlStatement)
                continue
    cnx.commit()
    cnx.close()
    print('finished loading database')



def getRidOfTags(input):
    newInput = re.sub('<(br|a|img|p|span|time)([^>]*)>', '', input)
    newInput = re.sub('(</a>|</p>|<ul>|</ul>|<li>|</li>|</span>|</time>|<em>|</em>|<strong>|</strong>)', '', newInput)
    return newInput

if __name__ == "__main__":
    nyTimesData = getNyTimesData()
    rssData = getAllData()
    createDatabaseConnection(nyTimesData, rssData)




