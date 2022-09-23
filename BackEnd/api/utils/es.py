from elasticsearch import Elasticsearch
from api.utils.settings import EnvVariables

envVariables = EnvVariables()

ES_HOST = envVariables.es_host
ES_PORT = envVariables.es_port

class ElasticSearchConnection():

    @staticmethod 
    def get_ESConnection():
        try:
            es = Elasticsearch([ES_HOST + ES_PORT])
            # yield?        
        finally:
            # if not es:  Me falta ver que pasa cuando no devuelve una conexion correcta
                return es
