from classify import *
from fs_watch import *
from add_to_index import *
from ConfigParser import SafeConfigParser

#Load config
parser = SafeConfigParser()
parser.read('config.ini')

#Connect to database
host = parser.get('elasticsearch', 'host')
port = parser.get('elasticsearch', 'port')
es = Elasticsearch([{'host': host, 'port': port}])

#Power up image recongizer
net, transformer = start_network()

#Get Images from fs_watcher
#
imagedir = raw_input("Full Path to directory of images > ")
for k in find_images(imagedir): 
    d = produce_data(k,net,transformer)
    for i in d:
        m = {}
        m['type'] = i
        m['predict'] = d[i]
        m['path'] = imagepath
        add_document(es, m)
