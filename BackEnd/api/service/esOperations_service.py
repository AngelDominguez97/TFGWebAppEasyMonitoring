from api.model.esOperations_model import ApiAccessModel
from api.utils.es import ElasticSearchConnection

es = ElasticSearchConnection.get_ESConnection()

def insertApiAccess(data: ApiAccessModel):
    response = es.index(index='access', document=data.json())
    return response

def getApiAccessByid(id: str):
    response = es.get(index='access', id=id)
    return response 

def refreshApiAccess(index: str):
    response = es.indices.refresh(index=index)
    return response

def searchAllApiAccess(index: str):
    response = es.search(index=index, query={'match_all': {}})
    return response

def updateApiAccessByid(id: str, index: str, data: ApiAccessModel):
    bodyJSON = data.json()
    # {"endpoint": "ProbandoUpdate", "dateTimeDone": "2022-09-02T11:33:09.826Z", "user": "angel"} 
    # Esta linea de arriba es un JSON funcional para el udpate  
    response = es.update(index=index, id=id, doc=bodyJSON.replace('\'', '')) 
    # Cuando envias algo serializado que viene de un modelo de pydantic, a la hora de generar 
    # el JSON lo devuelve dentro de unas comillas y al update de elastic no le gusta, se puede ver
    # dentro de la variable bodyJSON en tiempo de ejecucion  
    return response

def searchApiAccessByUser(user: str):
    response = es.search(index='access', query={'match': {"user": user}})
    return response 

def deleteDocumentApiAccess(id: str):
    reponse = es.delete(index='access', id=id)
    return reponse

def deleteIndexApiAccess(index: str):
    response = es.indices.delete(index=index, ignore=[400, 404])
    return response
