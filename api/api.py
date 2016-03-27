# main api file to serve api routes

# additional system paths
import sys
sys.path.insert(0, './data')


# imported modules
from flask import Flask, jsonify
from nyTimesHeadlines import nyTimesHeadlines

app = Flask(__name__)


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
