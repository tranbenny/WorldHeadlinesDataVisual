'''
useful functions for cleaning data in db
'''

from pymongo import MongoClient
from Config.DataSources import LOCAL_DB_URL
from Config.GetCountryNationalityTerms import get_nationalities

from DatabaseAccess.dao.CountriesDAO import CountriesDAO


def reformat_country_codes():
    '''
    removed new line character from all country code entries in countries collection
    :return:
    '''
    client = MongoClient(LOCAL_DB_URL)
    db = client['country']
    allCountries = db['countries'].find()
    for row in allCountries:
        country_code = row['country_code']
        country_code = country_code.replace('\n', '')
        db['countries'].update({
            '_id':row['_id']
        }, {
            '$set': {# updated values
                'country_code': country_code
            }
        })

    return None


def add_alternate_country_names():
    '''
    checks which country names differ from nationality list and country list
    :return:
    '''
    dao = CountriesDAO()
    countries_from_db = dao.__loadAllCountries__()
    countries_from_db = [x['country_name'] for x in countries_from_db]
    missed_countries_file = open('missed_countries.txt', 'w')
    countries = get_nationalities()
    for country in countries.keys():
        if country not in countries_from_db:
            missed_countries_file.write(country + '\n')
    missed_countries_file.close()


def _find_and_add_new_name_(db_name, new_name):
    client = MongoClient(LOCAL_DB_URL)
    db = client['country']
    db['countries'].update({
        'country_name': db_name
    }, {
        '$set': {
            'country_name': [db_name, new_name]
        }
    })


def add_missing_country_names():
    '''
    country names that are different in countries.csv and get_nationalities function:
        The United States
        Wales
        Democratic Republic of the Congo
        Britain
        The Philippines
        Republic of the Congo
        The United Arab Emirates
        the Czech Republic
        Scotland
        England
        Holland
        Ivory Coast
    :return:
    '''
    country_update_function_mapping = {
        'The United States': lambda x : _find_and_add_new_name_('United States', 'The United States'),
        # 'Wales' : lambda x: _find_and_add_new_name_('', 'Wales'),
        'Democratic Republic of the Congo' : lambda x: _find_and_add_new_name_('Congo - Kinshasa', 'Democratic Republic of the Congo'),
        'Britain' : lambda x : _find_and_add_new_name_('United Kingdom', 'Britain'),
        'The Philippines' : lambda x : _find_and_add_new_name_('Philippines', 'The Philippines'),
        'Republic of the Congo' : lambda x: _find_and_add_new_name_('Congo - Brazzaville', 'Republic of the Congo'),
        'The United Arab Emirates': lambda x : _find_and_add_new_name_('United Arab Emirates', 'The United Arab Emirates'),
        'the Czech Republic' : lambda x : _find_and_add_new_name_('Czech Republic', 'the Czech Republic'),
        # 'Scotland' : lambda x : _find_and_add_new_name_('', 'Scotland'),
        # 'England' : lambda x : _find_and_add_new_name_('', 'England'),
        # 'Holland' : lambda x : _find_and_add_new_name_('', 'Holland'),
        'Ivory Coast' : lambda x : _find_and_add_new_name_("Cote d'Ivoire", 'Ivory Coast')
    }


    with open('missed_countries.txt', 'r') as file:
        countries = file.readlines()
        countries = [x.replace('\n', '') for x in countries]
        for country in countries:
            if country in country_update_function_mapping.keys():
                country_update_function_mapping[country](3)
    file.close()





if __name__ == '__main__':
    # reformat_country_codes()
    # add_alternate_country_names()
    add_missing_country_names()
