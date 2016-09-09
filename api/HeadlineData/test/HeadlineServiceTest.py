'''

'''

import unittest
from HeadlineData.NyTimesHeadlineService import NyTimesHeadlineService
from HeadlineData.GetHeadlineService import GetHeadlineService


class HeadlineServiceTest(unittest.TestCase):

    def setUp(self):
        self.service = NyTimesHeadlineService()
        self.headlineService = GetHeadlineService()
        self.nyResults = self.service.getHeadlines() # list
        self.headlineResults = self.headlineService.getData() # dictionary


    def test_fetches_nytime_data_without_error(self):
        self.assertNotEqual(len(self.nyResults), 0)


    def tests_headline_service_completes_without_error(self):
        self.assertNotEqual(len(self.headlineResults), 0)


    def test_headline_data_is_right_format(self):
        # documents saved into mongoDB needs to be instance of dict, bson, bson.raw_bson, or inherits from
        # collections.MutableMapping
        for result in self.nyResults:
            self.assertTrue(isinstance(result, dict))
        for source in self.headlineResults.keys():
            for result in self.headlineResults[source]:
                self.assertTrue(isinstance(result, dict))



if __name__ == '__main__':
    unittest.main()