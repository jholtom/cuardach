from datetime import datetime
from elasticsearch import Elasticsearch

def produce_data(imagepath):
    image_data = transformer.preprocess('data', caffe.io.load_image(imagepath))
    x = predict(image_data)
    return x

def add_document(data):
    obj_type = data['type']
    predictions = data['predict']
    es.index(index="classifications", doc_type=obj_type, body={"file": imagepath, "timestamp": datetime.now(), "keywords" : predictions})
