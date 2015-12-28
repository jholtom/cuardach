from classify import *
from fs_watch import *
from add_to_index import * 
from ConfigParser import SafeConfigParser

#Load config
parser = SafeConfigParser()
parser.read('config.ini')

#Define important variables
imagenet_labels_filename = caffe_root + '/data/ilsvrc12/synset_words.txt'
labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

#Connect to database
host = parser.get('elasticsearch', 'host')
port = parser.get('elasticsearch', 'port')
es = Elasticsearch([{'host': host, 'port': port}])

#Power up image recongizer
net, transformer = start_network()

#Get Images from fs_watcher
#
#
#
# Temporary testing
imagepath = raw_input("Full Path to image > ")

#Get something to look at
print produce_data(imagepath,net,transformer)
