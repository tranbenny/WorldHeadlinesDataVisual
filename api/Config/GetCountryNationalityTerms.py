'''
- scrapes CIA World Factbook to get noun/adjective forms of countries
- returns dict object, key = country name, value = list of alternate noun/adj forms
'''

from nltk.tokenize.punkt import PunktLanguageVars
import requests
from bs4 import BeautifulSoup
from DatabaseAccess.service.CountriesService import CountriesService


URL = 'http://www.ef.com/english-resources/english-grammar/nationalities/'

tokenizer = PunktLanguageVars()

text = requests.get(URL).text
soup = BeautifulSoup(text, 'html.parser')

tables = soup.find_all('table')
# table[0]: geographic regions
# table[1]: country
# table[2]: specific cities

countries = tables[1]
country_names = {}


def validateWord(word):
    result = word
    result = result.replace('*', '')
    result = result.replace('person', '')
    if '(' in result:
        start = result.find('(')
        result = result[:start].strip()
    if '/' in result:
        tokens = result.split('/')
        return tokens
    else:
        return [result.strip()]


def extractInfo(info):
    names = info.find_all('td')
    country_name = names[0].text.strip()
    country_adj = names[1].text.strip()
    country_noun = names[2].text.strip()
    if country_noun.startswith('an '):
        country_noun = country_noun[3:]
    elif country_noun.startswith('a '):
        country_noun = country_noun[2:]
    country_noun = validateWord(country_noun)
    country_adj = validateWord(country_adj)
    country_names[country_name] = []
    for noun in country_noun:
        country_names[country_name].append(noun)
    for adj in country_adj:
        country_names[country_name].append(adj)


def get_nationalities():
    for row in countries.find('tbody').find_all('tr'):
        extractInfo(row)

    for name in country_names.keys():
        country_names[name] = set(country_names[name])

    return country_names



def add_nationality_terms_db():
    country_nationalities = get_nationalities()
    country_service = CountriesService()
    for country_name in country_nationalities.keys():
        terms = list(country_nationalities[country_name])
        country_service.addNewFieldToCountry({
            'country_name' : country_name
        }, {
            '$set' : {
                'other_names' : terms
            }
        })


if __name__ == '__main__':
    add_nationality_terms_db()








