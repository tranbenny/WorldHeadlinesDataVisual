from Flask import request, jsonify

from DatabaseAccess.service.HeadlineSummaryService import HeadlineSummaryService

service = HeadlineSummaryService()

# methods: GET
def getHeadlineSummaryData(date):
    countryResults = service.findByDate(date)
    return jsonify({
        'date': date,
        'country_results' : countryResults
    })

