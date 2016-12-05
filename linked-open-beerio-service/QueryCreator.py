from SemanticComponent import SemanticComponent
import Config as config

def create_query(action, parameters):
    """ Invokes sparql query creation for action"""
    return {
        'getBeerByStyle'    : create_beer_by_style_query,
        'getBeerByName'     : create_beer_by_name_query,
        'getBeerByBrewery'  : create_beer_by_brewery_query,
        'getBeerByCity'     : create_beer_by_city_query,
        'getBeerByCountry'  : create_beer_by_country_query,
        'getBreweryByCity'  : create_brewery_by_city_query,
        'getBreweryByCountry': create_brewery_by_country_query,
        'getStyleByName'    : create_style_by_name_query,
        'getBeer'           : create_beer_query,
        'getBreweryByName'  : create_brewery_by_name_query,
        'getBeerStyle'      : create_beerstyle_query
    }[action](parameters)


def create_beer_by_name_query(parameters):
    """ Returns a SPARQL query filled in with parameters"""
    query = """
           PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b, ?label, ?score, ?abv, ?style, ?brewery,?rank, ?stylecount  where {
            ?b rdfs:label ?y .
               OPTIONAL { ?b lob:hasScore ?score }
               ?b lob:hasABV ?abv .
               ?b lob:brewedBy ?breweryuri .
               ?b rdf:type ?styleuri.
               OPTIONAL { ?b lob:hasStyleRank ?rank }
               OPTIONAL { ?b lob:hasStyleCount ?stylecount }
            ?b rdfs:label ?label .
            ?styleuri rdfs:label ?style .
            ?breweryuri rdfs:label ?brewery .
            FILTER regex(?y, "%s", "i")
            } 
            limit 1
            """
    return query % parameters.get('beer-name').replace('...', '')

def create_beer_by_brewery_query(parameters):
    """ Returns a SPARQL query filled in with parameters"""
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b, ?label, ?score, ?brewery  where {
            ?bs rdfs:label ?y .
            ?b lob:brewedBy ?bs ;
               lob:hasScore ?score .
            ?b rdfs:label ?label .
            ?bs rdfs:label ?brewery .   
            FILTER regex(?y, "%s", "i")
            FILTER ( 1 >  <bif:rnd> (2, ?b)) 
            } 
            order by desc(?score)
            limit 3
            """
    return query % parameters.get('brewery-name').replace('...', '')

def create_style_by_name_query(parameters):
    """ Returns a SPARQL query filled in with parameters """
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?style, ?description  where {
            ?s rdfs:label "%s" .
            ?s rdfs:comment ?description.
            ?s rdfs:label ?style .
            } 
            """
    return query % parameters.get('style-name').replace('...', '')

def create_beer_by_country_query(parameters):
    """ Returns a SPARQL query filled in with parameters """
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
            select ?beer, ?label, ?score, ?locality  where {
            ?b vcard:hasCountryName ?y .

            ?beer lob:brewedBy ?b ;
                  lob:hasScore ?score .
            ?beer rdfs:label ?label.
            ?b vcard:hasCountryName ?locality .
            FILTER regex(?y, "%s", "i")
            FILTER ( 1 >  <bif:rnd> (2, ?beer)) 
            }
            order by desc(?score)
            limit 3
    """
    return query % parameters.get('beer-country').replace('...', '')

def create_beer_by_city_query(parameters):
    """ Returns a SPARQL query filled in with parameters """
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
            select ?beer, ?label, ?score, ?locality  where {
            ?b vcard:hasLocality ?y .

            ?beer lob:brewedBy ?b ;
                  lob:hasScore ?score .
            ?beer rdfs:label ?label.
            ?b vcard:hasLocality ?locality .
            FILTER regex(?y, "%s", "i")
            FILTER ( 1 >  <bif:rnd> (2, ?beer)) 
            }
            order by desc(?score)
            limit 3
    """
    return query % parameters.get('beer-city').replace('...', '')

def create_brewery_by_city_query(parameters):
    """ Returns a SPARQL query filled in with parameters """
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
            select ?b, ?label, ?locality  where {
            ?b vcard:hasLocality ?y .
            ?b rdfs:label ?label.
            ?b vcard:hasLocality ?locality .
            FILTER regex(?y, "%s", "i")
            FILTER ( 1 >  <bif:rnd> (2, ?b)) 
            }
            limit 3
    """
    return query % parameters.get('brewery-city').replace('...', '')

def create_brewery_by_country_query(parameters):
    """ Returns a SPARQL query filled in with parameters """
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
            select ?b, ?label, ?locality  where {
            ?b vcard:hasCountryName ?y .
            ?b rdfs:label ?label.
            ?b vcard:hasCountryName ?locality .
            FILTER regex(?y, "%s", "i")
            FILTER ( 1 >  <bif:rnd> (2, ?b)) 
            }
            limit 3
    """
    return query % parameters.get('brewery-country').replace('...', '')

def create_brewery_by_name_query(parameters):
    query = """
         PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX dpo: <http://dbpedia.org/ontology/>
            select ?brewery, ?abstract  where {
            ?bs rdfs:label ?y .
            ?bs a lob:Brewery.
            ?bs rdfs:label ?brewery .
            ?bs owl:sameAs ?x .
            SERVICE <http://dbpedia.org/sparql> { 
            ?x dpo:abstract ?abstract .
             FILTER (lang(?abstract) = 'en') .
            }
            FILTER regex(?y, "%s", "i") .
            } 
            limit 1
            """
    query = query % parameters.get('brewery-name').replace('...', '')
    SPARQL = SemanticComponent(config.SPARQL_LOB_ENDPOINT)
    data = SPARQL.query(query)
    if not data:
        query = create_brewery_by_name_alternative_query(parameters)
    return query


def create_brewery_by_name_alternative_query(parameters):
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX owl: <https://www.w3.org/TR/owl-ref/#>
            PREFIX dpo: <http://dbpedia.org/ontology/>
            PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
            select ?brewery, ?avgrating, ?country, ?city where {
            ?bs rdfs:label ?y .
            ?bs a lob:Brewery .
            ?bs rdfs:label ?brewery .
            OPTIONAL {?bs lob:hasAverageRating ?avgrating }
            OPTIONAL {?bs vcard:hasLocality ?city }
            OPTIONAL {?bs vcard:hasCountryName ?country }
            FILTER regex(?y, "%s", "i") .
  } 
    """
    return query % parameters.get('brewery-name').replace('...', '')

def create_beer_query(parameters):
    query_start = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b where {
            """
    query_end = """
            ?s a lob:BeerStyle .
            ?beer rdf:type ?s .
            ?beer a lob:Beer.
            ?beer rdfs:label ?b . 
            FILTER ( 1 >  <bif:rnd> (2, ?b)) 
            }
            limit 3
            """

    options = ''
    if parameters.get('beer-style-bitterness'):
        options += """
                    ?s lob:hasBitterness ?x .
                    FILTER regex(?x, "{}", "i") . 
                   """.format(parameters.get('beer-style-bitterness'))
    if parameters.get('beer-style-color'):
        options += """
                     ?s lob:hasColor ?y .
                     FILTER regex(?y, "{}", "i"). 
                     """.format(parameters.get('beer-style-color'))
    if parameters.get('beer-style-flavor'):
        options += """
                     ?s lob:hasFlavor ?z .
                     FILTER regex(?z, "{}", "i"). 
                     """.format(parameters.get('beer-style-flavor'))
    if parameters.get('beer-style'):
        options += """
                     ?s rdfs:label ?a .
                     FILTER regex(?a, "{}", "i"). 
                     """.format(parameters.get('beer-style'))
    if parameters.get('beer-country'):
        options += """
                   ?b vcard:hasCountryName "{}" .
                   ?beer lob:brewedBy ?b ;
                   """.format(parameters.get('beer-country'))
    query = query_start + options + query_end
    return query

def create_beer_by_style_query(parameters):
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?blabel, ?slabel, ?desc  where {
            ?s rdfs:label ?slabel .
            ?s a lob:BeerStyle . 
            ?s rdfs:comment ?desc .
            ?b a ?s ;
                lob:hasScore ?score .
            ?b rdfs:label ?blabel .
            FILTER regex(?slabel, "%s", "i"). 
            FILTER ( 1 >  <bif:rnd> (2, ?s))           
            }
            order by desc(?score)
            limit 3
            """
    return query % parameters.get('beer-style')

def create_beerstyle_query(parameters):
    query_start = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?label where {
            ?s rdfs:label ?label .
            """
    query_end = """
            FILTER ( 1 >  <bif:rnd> (2, ?s))           
            }
            limit 3
            """
    options = ''
    if parameters.get('beer-style-color'):
        options += """
                    ?s lob:hasColor ?y .
                    FILTER regex(?y, "{}", "i") . 
                   """.format(parameters.get('beer-style-color'))

    if parameters.get('beer-style-flavor'):
        options += """
                    ?s lob:hasFlavor ?x .
                    FILTER regex(?x, "{}", "i") . 
                   """.format(parameters.get('beer-style-flavor'))

    if parameters.get('beer-style-bitterness'):
        options += """
                    ?s lob:hasBitterness ?z .
                    FILTER regex(?z, "{}", "i") .
                   """.format(parameters.get('beer-style-bitterness'))

    query = query_start + options + query_end
    return query

