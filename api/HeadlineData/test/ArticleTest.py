import unittest

from HeadlineData.GetHeadlineService import GetHeadlineService


class ArticleTest(unittest.TestCase):

    def setUp(self):
        self.service = GetHeadlineService()

    def test_formatting_dates(self):
        sampleDate = "Thu 08 Sep 2016 16:02:40 -400"
        dateFormat = self.service.__formatRSSDate__(sampleDate)
        self.assertNotEqual(dateFormat, '%s-%s-%s')
        self.assertEqual(dateFormat, '2016-09-08')


if __name__ == '__main__':
    unittest.main()