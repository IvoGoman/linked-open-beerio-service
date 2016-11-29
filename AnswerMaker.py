

def create_answer(action, data):
    """ Invokes answer creation for data based on action"""
    if not data :
        return create_reply("Sorry, I did not what you are talking about.")
    return {
        'getBeerByStyle'    :   create_beer_by_style_answer,
        'getBeerByName'     :   create_beer_by_name_answer,
        'getBeerByBrewery'  :   create_beer_by_brewery_answer
    }[action](data)

def create_beer_by_style_answer(data):
    """ Makes an answer string containing data """
    title = "Which one do you like?"
    choices = []
    for x in data:
        choices.append(x['label']['value'])
    return create_quick_reply(title, choices)

def create_beer_by_name_answer(data):
    resp = "{} is a {} brewed by {} and has {}% ABV."
    resp = resp.format(data[0]['label']['value'], data[0]['style']['value'], data[0]['brewery']['value'], data[0]['abv']['value'])
    resp += " Furthermore it positions itself at rank {} out of {} {}s with a score of {}.".format(data[0]['rank']['value'],data[0]['stylecount']['value'], data[0]['style']['value'], data[0]['score']['value']) 
    return create_reply(resp)


def create_beer_by_brewery_answer(data):
    title = "These are the top 3 beers brewed by " + data[0]['brewery']['value'] + "."
    choices = []
    for x in data:
        choices.append(x['label']['value'])
    return create_quick_reply(title, choices)

def create_quick_reply(title, choices):
    """ Returns a fullfillment string for quick replies"""
    return {
        "speech": "",
        "messages":[
            {
                "title":title,
                "replies":
                    choices
                ,
                "type":2
            }
        ],
        # "data": data,
        # "contextOut": [],
        "source": "apiai-beerio-webhook-sample"
    }

def create_reply(text):
    return {
        "speech": text,
        "displayText": text,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }

