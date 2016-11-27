import json
import os
from flask import Flask
from flask import request
from flask import make_response
from SemanticComponent import SemanticComponent
import QueryCreator
import config

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print('Request: ' + json.dumps(req, indent=4))
    result = processRequest(req)
    result = json.dumps(result, indent=4)
    print(result)
    result_api = make_response(result)
    result_api.headers['Content-Type'] = 'application/json'
    return result_api


def processRequest(req):
    if req.get('result').get('action') not in config.API_AI_REQUESTS:
        print('ACTION not possible')
        return{}
    sparql_query = convertToSPARQL(req)
    if sparql_query is None:
        print('PARAMETERS not GOOD')
        return {}
    data = semantic_component.query(sparql_query)
    result = makeBeerioResult(data)
    return result

def convertToSPARQL(data):
    action = data.get('result').get('action')
    params = data.get('result').get('parameters')
    if params is None:
        return {}
    query = QueryCreator.createQuery(action, params)
    return query

def makeBeerioResult(data):
    result = data[0].get('result')
    if result is None:
        return {}
    speech = "The style you are looking for is from " + result.get('value')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-beerio-webhook-sample"
    }

if __name__ == '__main__':
    semantic_component = SemanticComponent(config.SPARQL_LOB_ENDPOINT)
    PORT = int(os.getenv('PORT', 5000))
    print("Starting beerio endpoint on port %d" % PORT)
    app.run(debug=False, port=PORT, host='0.0.0.0')
