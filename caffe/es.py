from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

f = open("/opt/caffe/data/ilsvrc12/synset_words.txt")
for line in f:
    type = line.split()[0]
    es.index(index='classifcations', doc_type=type)
