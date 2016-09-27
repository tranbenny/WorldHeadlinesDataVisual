# main application serving web content and data

from flask_cors import cross_origin

import time
from flask import Flask, request, jsonify, Response, render_template, url_for
from flask.ext.cors import CORS

from DatabaseAccess.service.HeadlineSummaryService import HeadlineSummaryService



app = Flask(__name__)
CORS(app)
cross_origin(app)

service = HeadlineSummaryService()

# API ROUTES
# -------------------------------------------------------------------------------------------

@app.route('/api/sample', methods=['GET'])
def getSample():
    return jsonify(service.getSampleData())


@app.route('/api/headlines', methods=['GET'])
def getHeadlines():
     date = request.args.get('date')
     return jsonify(service.findByDate(date))


@app.route('/api/headlines/today', methods=['GET'])
def getTodayHeadlines():
     date = time.strftime('%Y-%m-%d')
     return jsonify(service.findByDate(date))



if __name__ == '__main__':
    app.debug = True # REMEMBER TO TURN OFF FOR PRODUCTION
    app.run()
