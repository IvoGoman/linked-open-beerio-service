def create_query(action, parameters):
    """ Invokes sparql query creation for action"""
    return {
        'getBeerByStyle'    : create_beer_by_style_query(parameters),
        'getBeerByName'     : create_beer_by_name_query(parameters),
        'getBeerByBrewery'  : create_beer_by_brewery_query(parameters) 
    }[action]


def create_style_query(parameters):
    """ Returns a SPARQL query filled in with parameters"""
    query = """
            PREFIX lod: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX sty: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/styles/>
            select ?result WHERE { 
            ?result a lod:BeerStyles .
            ?result rdfs:label "%s".
            }  limit 100
            """

    return query % parameters.get('beer-style')

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
            } 
            order by desc(?score)
            limit 3
            """
    return query % parameters.get('beer-style')

def create_beer_by_name_query(parameters):
    """ Returns a SPARQL query filled in with parameters"""
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b, ?label, ?score, ?abv, ?style, ?brewery  where {
            ?b rdfs:label ?y ;
                lob:hasScore ?score ;
                lob:hasABV ?abv;
                lob:hasStyle ?style;
                lob:brewedBy ?brewery .
            ?b rdfs:label ?label .
            FILTER regex(?y, "%s", "i")
            } 
            limit 1
            """
    return query % parameters.get('beer-name')

def create_beer_by_brewery_query(parameters):
    """ Returns a SPARQL query filled in with parameters"""
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b, ?label, ?score, ?bs  where {
            ?bs rdfs:label ?y .
            ?b lob:brewedBy ?bs ;
                lob:hasScore ?score .
            ?b rdfs:label ?label .
            FILTER regex(?y, "%s", "i")
            } 
            order by desc(?score)
            limit 3
            """
    return query % parameters.get('brewery-name')
