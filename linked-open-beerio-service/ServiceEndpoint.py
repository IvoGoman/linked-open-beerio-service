import json
import os
from flask import Flask
from flask import request
from flask import make_response
from SemanticComponent import SemanticComponent
import QueryCreator
import AnswerMaker
import Config as config

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    """ Receives and processes requests from api.ai  """
    req = request.get_json(silent=True, force=True)
    print('Request: ' + json.dumps(req, indent=4))
    result = process_request(req)
    result = json.dumps(result, indent=4)
    result_api = make_response(result)
    result_api.headers['Content-Type'] = 'application/json'
    return result_api


def process_request(req):
    """ Processes req and returns fullfillment """
    action = req.get('result').get('action')
    if action not in config.API_AI_REQUESTS:
        print('ACTION not possible')
        return{}
    sparql_query = convert_to_sparql(req)
    if sparql_query is None:
        print('PARAMETERS not GOOD')
        return {}
    data = SEMANTIC_COMPONENT.query(sparql_query)
    result = make_beerio_result(action, data)
    return result

def convert_to_sparql(data):
    """ Return a SPARQL Query corresponding to the Data """
    action = data.get('result').get('action')
    params = data.get('result').get('parameters')
    if params is None:
        return {}
    query = QueryCreator.create_query(action, params)
    return query

def make_beerio_result(action, data):
    """ Returns a answer string for an action from data"""
    if data is None:
        return {}
    fullfillment = AnswerMaker.create_answer(action, data)

    print("Response:")
    print(fullfillment)

    return fullfillment

if __name__ == '__main__':
    SEMANTIC_COMPONENT = SemanticComponent(config.SPARQL_LOB_ENDPOINT)
    PORT = int(os.getenv('PORT', 5000))
    print("Starting beerio endpoint on port %d" % PORT)
    app.run(debug=False, port=PORT, host='0.0.0.0')
