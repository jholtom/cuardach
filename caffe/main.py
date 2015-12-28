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
start_network()

#Get Images from fs_watcher
#
#
#
# Temporary testing
imagepath = raw_input("Full Path to image > ")

#Get something to look at
print produce_data(imagepath)
