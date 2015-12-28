from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

type = "n0111231" # get from classifcations
predictions = {} # build this from the output of predict()
es.index(index="classifications", doc_type=type, body={"file": imagepath, "timestamp": datetime.now(), "keywords" : predictions})
