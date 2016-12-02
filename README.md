# linked-open-beer-beerio-service
This service creates SPARQL queries based on the requests send by beerio, our chatbot on api.ai.
The result of these queries is then put into a format that can be displayed to the user.

## How to use
- python3 ServiceEndpoint.py
- make sure that port 5000 is open, as the webhook communicates via this port

## Intents Implemented
- getBeerByStyle(beer-style)
- getBeerByBrewery(brewery-name)
- getBeerByName(beer-name)
- getStyleByName(style-name)
- getBreweryByCountry(brewery-country)
- getBeerByCity(beer-city)
- getBeerByCountry(beer-country)
- getBreweryByCity(brewery-city)
- getBeer(beer-style-color, beer-style-flavor, beer-style-bitterness, beer-country, beer-style)
- getBreweryByName(brewery-name)

## Intents TODOs
- getBeerStyle(beer-style-color, beer-style-flavor, beer-style-bitterness)