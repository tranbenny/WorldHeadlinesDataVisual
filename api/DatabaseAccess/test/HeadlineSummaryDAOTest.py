import unittest

from DatabaseAccess.dao.HeadlineSummaryDAO import HeadlineSummaryDAO

class HeadlineSummaryDAOTest(unittest.TestCase):

    def setUp(self):
        self.dao = HeadlineSummaryDAO()

    def test_basic_result_fetching(self):
        validDate = '2016-09-08'
        countryResults = self.dao.findByDate(validDate)
        self.assertIsNotNone(countryResults)
        self.assertIsInstance(countryResults, dict)

    def test_only_finds_one_result(self):
        validDate = '2016-09-08'
        cursor = self.dao.__findAll__(validDate)
        self.assertEquals(cursor.count(), 1)



if __name__ == '__main__':
    unittest.main(verbosity=2)