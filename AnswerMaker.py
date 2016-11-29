

def create_answer(action, data):
    """ Invokes answer creation for data based on action"""
    return {
        'getBeerByStyle'    :   create_beer_by_style_answer(data),
        'getBeerByName'     :   create_beer_by_name_answer(data),
        'getBeerByBrewery'  :   create_beer_by_brewery_answer(data)
    }[action]

def create_beer_by_style_answer(data):
    """ Makes an answer string containing data """
    title = "Which one do you like?"
    choices = []
    for x in data:
        choices.append(x['label']['value'])
    return create_quick_reply(title, choices)

def create_beer_by_name_answer(data):
    display_text = "%s is a %s brewed by %s and has %s°%"
    display_text = display_text % (data[0]['label']['value'], data[0]['style']['value'], data[0]['brewery']['value'], data[0]['abv']['value'])
    return create_reply(display_text)

def create_beer_by_brewery_answer(data):
    title = "These are the top 3 beers brewed by " + data[0]['bs']['value'] + "."
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

