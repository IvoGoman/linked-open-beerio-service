

def createAnswer(action, data):
    return {
        'getBeerByStyle' : createBeerByStyleAnswer(data)
    }[action]

def createBeerByStyleAnswer(data):
    title = "Which one do you like?"
    choices =''
    for x in data:
        choices += '"' + x['label']['value'] + '", '
    choices = choices[:-2]

    return {
        "speech": "",
        "messages":[
            {
                "title":title,
                "replies":[
                    choices
                ],
                "type":2
            }
        ],
        # "data": data,
        # "contextOut": [],
        "source": "apiai-beerio-webhook-sample"
    }

