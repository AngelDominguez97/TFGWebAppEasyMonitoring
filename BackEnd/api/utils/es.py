from elasticsearch import Elasticsearch
from api.utils.settings import Settings

settings = Settings()

ES_HOST = settings.es_host
ES_PORT = settings.es_port

class ElasticSearchConnection():

    @staticmethod 
    def get_ESConnection():
        try:
            es = Elasticsearch([ES_HOST + ES_PORT])
            # yield?        
        finally:
            # if not es:  Me falta ver que pasa cuando no devuelve una conexion correcta
                return es
