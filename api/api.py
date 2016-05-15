'''
api routes:
/today
/:<date>

'''

# main api file to serve api routes


# additional system paths for other folders
import sys

from flask_cors import cross_origin

sys.path.insert(0, './data')

# imported modules
from flask import Flask, jsonify, Response
from flask.ext.cors import CORS
from getHeadlines import readFromDatabase



app = Flask(__name__)
CORS(app)
cross_origin(app)


# main application routes
@app.route('/')
def hello():
    return 'hello world!'

# api route for getting today's date headlines
@app.route('/today', methods=['GET'])
@cross_origin()
def getHeadlines():
    results = {}
    results['data'] = readFromDatabase()
    if len(results['data']) != 0:
        response = jsonify(results)
        response.status_code = 200
        return response
    else:
        return notFound()

# api route for handling unhandled routes

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
    app.debug = True
    app.run()
