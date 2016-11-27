from SPARQLWrapper import SPARQLWrapper, JSON
import config
import logging

class SemanticComponent():

    def __init__(self, endpoint):
        self.endpoint = SPARQLWrapper(endpoint)

    def query(self, statement):
        self.endpoint.setQuery(statement)
        self.endpoint.setReturnFormat(JSON)
        return self.endpoint.query().convert()['results']['bindings']
