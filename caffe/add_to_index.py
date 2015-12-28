from datetime import datetime
from elasticsearch import Elasticsearch

def add_document(es, data):
    imagepath = data['path']
    obj_type = data['type']
    prediction = data['predict']
    es.index(index="classifications", doc_type=obj_type, body={"file": imagepath, "timestamp": datetime.now(), "keywords" : prediction})
