def createQuery(action, parameters):
    return {
        'getStyleDescription' : createStyleQuery(parameters)
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


#       query = """
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     SELECT ?label
#     WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
# """
#     return query