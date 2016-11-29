def create_answer(action, data):
    """ Invokes answer creation for data based on action"""
    if not data :
        return create_reply("Sorry, I did not what you are talking about.")
    return {
        'getBeerByStyle'    :   create_beer_by_style_answer,
        'getBeerByName'     :   create_beer_by_name_answer,
        'getBeerByBrewery'  :   create_beer_by_brewery_answer,
        'getBeerByCity'     :   create_beer_by_locality_answer,
        'getBeerByCountry'  :   create_beer_by_locality_answer,
        'getBreweryByCity'  :   create_brewery_by_locality_answer,
        'getBreweryByCountry':   create_brewery_by_locality_answer,
        'getStyleByName'    :   create_style_by_name_answer
    }[action](data)

def create_beer_by_style_answer(data):
    """ Makes an answer string containing data """
    title = "Which one do you like?"
    choices = []
    for x in data:
        choices.append(x['label']['value'])
    return create_quick_reply(title, choices)

def create_beer_by_name_answer(data):
    """ Makes an answer string containing data """
    resp = "{} is a {} brewed by {} and has {}% ABV."
    resp = resp.format(data[0]['label']['value'], data[0]['style']['value'],\
            data[0]['brewery']['value'], data[0]['abv']['value'])
    resp += " Furthermore it positions itself at rank {} out of {} {}s with a score of {}."\
            .format(data[0]['rank']['value'], data[0]['stylecount']['value'], \
            data[0]['style']['value'], data[0]['score']['value'])
    return create_reply(resp)


def create_beer_by_brewery_answer(data):
    """ Makes an answer string containing data """
    title = "These are the top 3 beers brewed by " + data[0]['brewery']['value'] + "."
    choices = []
    for x in data:
        choices.append(x['label']['value'])
    return create_quick_reply(title, choices)

def create_style_by_name_answer(data):
    """ Makes an answer string containing data """
    text = data[0]["style"]["value"]
    return create_reply(text)

def create_beer_by_country_answer(data):
    """ Makes an answer string containing data """
    text = "These are the top beers brewed in " + data[0]['country']['value'] + ": "
    for x in data:
        text += x['label']['value'] + ", "
    return create_reply(text[:-2]+".")

def create_beer_by_locality_answer(data):
    """ Makes an answer string containing data """
    text = "These are beers brewed in " + data[0]['locality']['value'] + ": "
    for x in data:
        text += x['label']['value'] + ", "
    return create_reply(text[:-2]+".")

def create_brewery_by_locality_answer(data):
    """ Makes an answer string containing data """
    text = "These are breweries that are located in " + data[0]['locality']['value'] + ": "
    for x in data:
        text += x['label']['value'] + ", "
    return create_reply(text[:-2]+".")


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
    """ Returns a fullfillment string for simple replies"""
    return {
        "speech": text,
        "displayText": text,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }

