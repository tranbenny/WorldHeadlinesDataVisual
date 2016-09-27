'''
main script for populating database with headline data

TODO:
- formulate to run regularly with AWS Lambda
- create a progress bar that prints in console?
'''

import time

from DatabaseAccess.service.HeadlineService import HeadlineService
from HeadlineData.GetHeadlineService import GetHeadlineService
from HeadlineData.NyTimesHeadlineService import NyTimesHeadlineService

if __name__ == '__main__':
    headlineDate = time.strftime('%Y-%m-%d')
    headlineService = GetHeadlineService()
    service = HeadlineService()
    nyTimesService = NyTimesHeadlineService()

    results = headlineService.getData()
    nyResults = nyTimesService.getHeadlines()

    service.saveMultiple(nyResults, headlineDate)
    service.saveMultiple(results, headlineDate)

    # TODO: update country list after fetching headlines


    print('DONE')