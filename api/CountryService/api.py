'''

'''

from CountryService.CountriesDAO import CountriesDAO

dao = CountriesDAO()

def locateCountry(text):
    return dao.locateCountry(text)