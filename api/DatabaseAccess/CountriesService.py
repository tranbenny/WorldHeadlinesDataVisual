from DatabaseAccess.CountriesDAO import CountriesDAO

class CountriesService:

    def __init__(self):
        self.countriesDAO = CountriesDAO()

    def locateCountry(self, text):
        '''
        :param text:
        :return:
        '''
        return self.countriesDAO.locateCountry(text)

