from datetime import datetime
from elasticsearch import Elasticsearch

def add_document(data):
    obj_type = data['type']
    predictions = data['predict']
    es.index(index="classifications", doc_type=obj_type, body={"file": imagepath, "timestamp": datetime.now(), "keywords" : predictions})
