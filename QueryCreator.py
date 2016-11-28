def createQuery(action, parameters):
    return {
        'getBeerByStyle' : createBeerByStyleQuery(parameters)
    }[action]


def createStyleQuery(parameters):
    query = """
            PREFIX lod: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            PREFIX sty: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/styles/>
            select ?result WHERE { 
            ?result a lod:BeerStyles .
            ?result rdfs:label "%s".
            }  limit 100
            """
  
    return (query % parameters.get('beer-style'))

def createBeerByStyleQuery(parameters):
    query = """
            PREFIX lob: <http://dws.informatik.uni-mannheim.de/swt/linked-open-beer/ontology/>
            select ?b ?label ?score where {
            ?bs rdfs:label "%s" .
            ?b lob:hasStyle ?bs ;
                lob:hasScore ?score .
            ?b rdfs:label ?label .
            } 
            order by desc(?score)
            limit 3
            """
  
    return (query % parameters.get('beer-style'))

#       query = """
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     SELECT ?label
#     WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
# """
#     return query