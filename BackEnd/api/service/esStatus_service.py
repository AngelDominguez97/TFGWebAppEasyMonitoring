from api.utils.es import ElasticSearchConnection
import requests

es = ElasticSearchConnection.get_ESConnection()

def getEsClusterStatus():
    response = requests.get("http://10.57.36.249:9200/_cluster/health")
    return response.json()['status']