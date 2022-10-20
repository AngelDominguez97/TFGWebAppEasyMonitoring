from operator import concat
from api.utils.es import ElasticSearchConnection
import requests
from api.utils.settings import EnvVariables

envVariables = EnvVariables()

ES_HOST = envVariables.es_host
ES_PORT = envVariables.es_port
es = ElasticSearchConnection.get_ESConnection()

def getEsClusterStatus():
    url = concat(ES_HOST, ES_PORT)
    response = requests.get(url + "/_cluster/health")
    return response.json()['status']

def getEsClusterHealth():
    url = concat(ES_HOST, ES_PORT)
    response = requests.get(url + "/_cluster/health?pretty")
    return response.text