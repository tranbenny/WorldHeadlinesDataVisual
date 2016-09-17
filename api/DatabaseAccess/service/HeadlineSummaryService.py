from DatabaseAccess.dao.HeadlineSummaryDAO import HeadlineSummaryDAO

class HeadlineSummaryService:

    def __init__(self):
        self.dao = HeadlineSummaryDAO()

    def findByDate(self, date):
        return self.dao.findByDate(date)