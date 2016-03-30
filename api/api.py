# main api file to serve api routes

# additional system paths for other folders
import sys
sys.path.insert(0, './data')

# imported modules
from flask import Flask, jsonify
from flask.ext.cors import CORS
from nyTimesHeadlines import nyTimesHeadlines

app = Flask(__name__)
CORS(app)


# main application routes
@app.route('/')
def hello():
    return 'hello world!'

@app.route('/headlines', methods=['GET'])
def getHeadlines():
    response = nyTimesHeadlines().getData()
    return jsonify({'results' : response})



if __name__ == '__main__':
    app.debug = True
    app.run()
