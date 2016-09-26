'''
sample file for testing countries
- write title, description and located countries in a file
'''

from pymongo import MongoClient
from Config.DataSources import LOCAL_DB_URL
from DatabaseAccess.service.CountriesService import CountriesService


headline_sample_file = open('headline_country.txt', 'w')


country_service = CountriesService()

# get random articles
client = MongoClient(LOCAL_DB_URL)
db = client['headlines']
sample_headlines = db['2016-09-08'].find()

counter = 0

for headline in sample_headlines:
    if (counter == 20):
        quit()
    title = str(headline['title'])
    description = str(headline['description'])
    countries = country_service.locateCountry(title)
    countries.extend(country_service.locateCountry(description))
    print(title)
    print(description)
    print(countries)
    try:
        headline_sample_file.write('TITLE: ' + title + "\n")
        headline_sample_file.write('DESCRIPTION: ' + description + "\n")
        headline_sample_file.write('COUNTRIES: ' + str(countries) + "\n")
    except UnicodeEncodeError as e:
        print('DIDNT PRINT')
        print(title)
        print(description)
        print(countries)

    counter += 1



headline_sample_file.close()