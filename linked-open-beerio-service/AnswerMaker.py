def create_answer(action, data):
    """ Invokes answer creation for data based on action"""
    if not data:
        return create_reply("Sorry lad, I had a few too many and cannot remember the answer.")
    return {
        'getBeerByStyle'    :   create_beer_by_style_answer,
        'getBeerByName'     :   create_beer_by_name_answer,
        'getBeerByBrewery'  :   create_beer_by_brewery_answer,
        'getBeerByCity'     :   create_beer_by_locality_answer,
        'getBeerByCountry'  :   create_beer_by_locality_answer,
        'getBreweryByCity'  :   create_brewery_by_locality_answer,
        'getBreweryByCountry':   create_brewery_by_locality_answer,
        'getStyleByName'    :   create_style_by_name_answer,
        'getBeer'           :   create_beer_answer,
        'getBeerStyle'      :   create_beerstyle_answer,
        'getBreweryByName'  :   create_brewery_by_name_answer
    }[action](data)

def create_beer_by_name_answer(data):
    """ Makes an answer string containing data """
    resp = "{} is a {} brewed by {} and has {}% ABV."
    resp = resp.format(data[0]['label']['value'], data[0]['style']['value'],\
            data[0]['brewery']['value'], data[0]['abv']['value'])
    if 'score' in data[0] and 'rank' in data[0] and 'stylecount' in data[0]:
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
    if data[0]['description']['value']:
        text = data[0]['description']['value']
    else:
        text = "Sorry lad I don't know anything about " + data[0]['style']['value']
    return create_reply(text)

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

def create_beer_answer(data):
    """ Makes an answer string containing data """
    text = "These beers match your criteria: "
    choices = []
    for x in data:
        text += x['b']['value'] + ", "
        choices.append(x['b']['value'])
    return create_quick_reply(text[:-2]+".", choices)

def create_beer_by_style_answer(data):
    text = """{}. These are the three best {}s that I could find for you:
            {}, {}, and {}. Which one would you like?"""
    text = text.format(data[0]['desc']['value'], data[0]['slabel']['value'],\
        data[0]['blabel']['value'], data[1]['blabel']['value'], data[2]['blabel']['value'])
    choices = []
    for x in data:
        choices.append(x['blabel']['value'])

    return create_quick_reply(text, choices)

def create_beerstyle_answer(data):
    text = "Based on your criteria I found the following beer styles: "
    choices = []
    for x in data:
        text += x['label']['value'] + ", "
        choices.append(x['label']['value'])
    text = text[:-2] + " Which one would you like to know more about?"
    return create_quick_reply(text, choices)

def create_brewery_by_name_answer(data):
    item = data[0]
    text = ''
    if 'abstract' in item:
        text += data[0]['abstract']['value']
        text.encode('utf-8')
    elif 'city' in item and 'country' in item:
        text += item['brewery']['value'] + "is a brewery. "
        text += "It is located in {}, {}.".format(item['city']['value'], item['country']['value'])

    return create_reply(text)

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

