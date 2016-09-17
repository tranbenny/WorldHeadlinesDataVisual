# main application serving web content and data

from flask_cors import cross_origin

import time
from flask import Flask, request, jsonify, Response
from flask.ext.cors import CORS


from HeadlineDataSummaryAPI.routes import getHeadlineSummaryData


app = Flask(__name__)
CORS(app)
cross_origin(app)

# API ROUTES
# -------------------------------------------------------------------------------------------
@app.route('/api/headlines', methods=['GET'])
@cross_origin()
def getHeadlines():
    date = request.args.get('date')
    return getHeadlineSummaryData(date)


@app.route('/api/headlines/today', method=['GET'])
@cross_origin()
def getTodayHeadlines():
    date = time.strftime('%Y-%m-%d')
    return getHeadlineSummaryData(date)



# WEB APPLICATION ROUTES
# -------------------------------------------------------------------------------------------
@app.route('/')
def hello():
    return 'hello world!'


@app.errorhandler(404)
def notFound():
    message = {
        'status': 404,
        'message' : 'Route not found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == '__main__':
    app.debug = True # REMEMBER TO TURN OFF FOR PRODUCTION
    app.run()
