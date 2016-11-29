def create_query(action, parameters):
    """ Invokes sparql query creation for action"""
    return {
        'getBeerByStyle'    : create_beer_by_style_query,
        'getBeerByName'     : create_beer_by_name_query,
        'getBeerByBrewery'  : create_beer_by_brewery_query
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
            } 
            order by desc(?score)
            limit 3
            """
    return query % parameters.get('brewery-name').replace('...', '')
