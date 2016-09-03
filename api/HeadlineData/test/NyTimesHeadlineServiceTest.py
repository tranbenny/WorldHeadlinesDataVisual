'''

'''

import unittest
from HeadlineData.NyTimesHeadlineService import NyTimesHeadlineService


class NyTimesHeadlineServiceTest(unittest.TestCase):

    def setUp(self):
        self.service = NyTimesHeadlineService()

    def test_fetches_nytime_data(self):
        headlines = self.service.getHeadlines()
        self.assertNotEqual(len(headlines), 0)

