import shutil
import tempfile
import os
import numpy as np
caffe_root = '/opt/caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
imagenet_labels_filename = caffe_root + '/data/ilsvrc12/synset_words.txt'
labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

def load_model():
    BATCH_SIZE = 12
    net = caffe.Net('/opt/caffe/models/bvlc_googlenet/deploy.prototxt',
                    '/models/bvlc_googlenet.caffemodel',
                    caffe.TEST)
    # change batch size to 1 for faster processing
    # this just means that we're only processing one image at a time instead of like 50
    # At scale, it may make more sense to do more simultaneously as # of cores increases
    shape = list(net.blobs['data'].data.shape)
    shape[0] = BATCH_SIZE
    net.blobs['data'].reshape(*shape)
    net.blobs['prob'].reshape(BATCH_SIZE, )
    net.reshape() 
    return net

def display(data):
    print transformer.deprocess('data', data)

def get_label_name(num):
    options = labels[num].split(',')
    # remove the tag
    options[0] = ' '.join(options[0].split(' ')[1:])
    return ','.join(options[:2])
    
def predict(data, net, n_preds=3):
    net.blobs['data'].data[...] = data
    prob = net.forward()['prob']
    probs = prob[0]
    prediction = probs.argmax()
    wtop_k = probs.argsort()[::-1]
    targ = {}
    for pred in top_k[:n_preds]:
        percent = round(probs[pred] * 100, 2)
        targ[pred] = {"labels": get_label_name(pred), "certainty": percent}
    return targ

def start_network():
    caffe.set_mode_cpu()
    net = load_model()
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
    transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB
    return (net, transformer)

def produce_data(imagepath,net,transformer):
    image_data = transformer.preprocess('data', caffe.io.load_image(imagepath))
    return predict(image_data,net)
