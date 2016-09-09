import unittest

from DatabaseAccess.HeadlineDAO import HeadlineDAO

class HeadlineDAOTest(unittest.TestCase):

    def setUp(self):
        self.dao = HeadlineDAO()

    def test_gets_headlines_with_valid_date(self):
        validDate = '2016-09-08'
        results = self.dao.findByDate(validDate)
        self.assertIsNotNone(results, "query should not be empty")
        self.assertNotEqual(results, 0)
        for headline in results:
            print(str(headline))
            self.assertEquals(headline['headline_date'], validDate, "found article with id " + str(headline['_id']) + " with the wrong date")

    def test_should_not_get_headlines_with_invalid_date(self):
        invalidDate = 'ldskfndlfn'
        results = self.dao.findByDate(invalidDate)
        self.assertEquals(results.count(), 0)


if __name__ == '__main__':
    unittest.main()