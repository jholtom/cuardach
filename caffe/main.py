from classify import *
from fs_watch import *
from add_to_index import *
import json
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
# This should eventually collect images and be a daemon, but hell, not yet
# 
# 
# 
# This works if you don't already have a list
#imagedir = raw_input("Full Path to directory of images > ")
#imglist = find_images(imagedir)
imagetxt = raw_input("Path to file with json list of directories >")
imglist = json.load(open(imagetxt,'r').read())
for k in imglist: 
    d = produce_data(k,net,transformer)
    for i in d:
        m = {}
        m['type'] = i
        m['predict'] = d[i]
        m['path'] = imagepath
        add_document(es, m)
