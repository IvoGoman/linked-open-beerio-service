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
        'getBeer'           : create_get_beer_query
    }[action](parameters)

def create_beer_by_style_query(parameters):
    """ Returns a SPARQL query filled in with parameters"""
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b ?label ?score where {
            ?bs rdfs:label ?y .
            ?b lob:hasStyle ?bs ;
                lob:hasScore ?score .
            ?b rdfs:label ?label .
            FILTER regex(?y, "%s", "i")
             FILTER ( 1 >  <bif:rnd> (2, ?b)) .
            }
            order by desc(?score)
            limit 3
            """
    return query % parameters.get('beer-style').replace('...', '')

def create_beer_by_name_query(parameters):
    """ Returns a SPARQL query filled in with parameters"""
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b, ?label, ?score, ?abv, ?style, ?brewery,?rank, ?stylecount  where {
            ?b rdfs:label ?y ;
                lob:hasScore ?score ;
                lob:hasABV ?abv;
                lob:hasStyle ?styleuri;
                lob:brewedBy ?breweryuri ;
                lob:hasStyleRank ?rank;
                lob:hasStyleCount ?stylecount.
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
            select ?s, ?description  where {
            ?s rdfs:label "%s" .
            ?s rdfs:comment ?description.
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

# TODO: Extend Query with the owl:sameAs Property to get the Abstract from DBpedia 
def create_brewery_by_name_query(parameters):
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX owl: <https://www.w3.org/TR/owl-ref/#>
            PREFIX dpo: <http://dbpedia.org/ontology/>
            select *  where {
            ?bs rdfs:label ?y .
            ?bs a lob:Brewery.
            ?bs rdfs:label ?brewery .
            dbo:?y (owl:sameAs|^owl:sameAs) ?x .
            FILTER regex(?y, "Eichbaum", "i") .
            } 
            limit 3
            """
    return query % parameters.get('brewery-name').replace('...', '')

def create_get_beer_query(parameters):
    query_start = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b where {
            """
    query_end = """
            ?s a lob:BeerStyles .
            ?beer rdf:type ?s .
            ?beer a lob:Beer.
            ?beer rdfs:label ?b . 
            FILTER ( 1 >  <bif:rnd> (2, ?beer)) 
            }
            limit 3
            """
            
    options = ''
            # , beer-style-flavor, beer-style-bitterness, beer-country, beer-style
    if parameters.get('beer-style-bitterness'):
        options += """ 
                    ?s lob:bitternes ?x .
                    FILTER regex(?x, "{}", "i") . 
                   """.format(parameters.get('beer-style-bitterness'))
    if parameters.get('beer-style-color'):
        options += """ 
                     ?s lob:color ?y .
                     FILTER regex(?y, "{}", "i"). 
                     """.format(parameters.get('beer-style-color'))
    if parameters.get('beer-style-flavor'):
        options += """ 
                     ?s lob:flavor ?z .
                     FILTER regex(?z, "{}", "i"). 
                     """.format(parameters.get('beer-style-flavor'))
    if parameters.get('beer-style'):
        options += """ 
                     ?s rdfs:label ?a .
                     FILTER regex(?a, "{}", "i"). 
                     """.format(parameters.get('beer-style'))
    if parameters.get('beer-country'):
        options += """
                   ?b vcard:hasCountryName ?c .
                   ?beer lob:brewedBy ?b ;
                   """.format(parameters.get('beer-country'))
    query = query_start + options + query_end
    print(query)
    return query

