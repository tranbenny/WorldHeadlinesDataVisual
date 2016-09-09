'''
main script for populating database with headline data

TODO:
- formulate to run regularly with AWS Lambda
- create a progress bar that prints in console?
'''

from HeadlineData.GetHeadlineService import GetHeadlineService
from DatabaseAccesss.HeadlineService import HeadlineService

if __name__ == '__main__':
    headlineService = GetHeadlineService()
    results = headlineService.getData()
    service = HeadlineService()
    service.saveMultiple(results, 'headlines')
    print('DONE')