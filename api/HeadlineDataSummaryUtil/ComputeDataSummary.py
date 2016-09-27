from pymongo import MongoClient

from Config.DataSources import LOCAL_DB_URL
from DatabaseAccess.service.HeadlineService import HeadlineService


def computeDateSummary(date):
    '''
    :param date: String date
    :return: computes data summary and saves to database
    '''

    # database variables
    client = MongoClient(LOCAL_DB_URL)
    db = client['headline_summary']
    headlineService = HeadlineService()

    try:
        results = headlineService.findByDate(date)
    except:
        # collection not found error
        raise Exception("Collection doesn't exist")

    countryCount = {}
    # variables: date, count for every country
    for result in results:
        countries = result['countries']
        for country in countries:
            if country not in countryCount.keys():
                countryCount[country] = 1
            else:
                countryCount[country] += 1


    countryCount.pop(None, None)
    countryDocument = {
        'date': date,
        'count': countryCount
    }

    # save results to mongo db
    db['country_count'].insert_one(countryDocument)

