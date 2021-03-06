'''
console function to show how well the country scraping works
'''


from CountrySerivce.api import locateCountry
from DatabaseAccess.service.HeadlineService import HeadlineService


headline_service = HeadlineService()

headlines = headline_service.findByDate('2016-09-08')

issues_text = open('issues.txt', 'w')

for headline in headlines:
    title = headline['title']
    description = headline['description']
    countries = locateCountry(title)
    countries.extend(locateCountry(description))
    print('TITLE')
    print(title)
    print("DESCRIPTION")
    print(description)
    print('COUNTRIES')
    print(countries)
    correct = input('Is the correct? (y/n)')
    if (correct == 'n'):
        title = str(title.encode('utf-8'))
        issues_text.write(title)
        issues_text.write('\n')


issues_text.close()