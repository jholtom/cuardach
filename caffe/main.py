from classify import *
from fs_watch import *
from add_to_index import * 
imagepath = raw_input('Full Path to image to classify > ')
image_data = transformer.preprocess('data', caffe.io.load_image(imagepath))

predict(image_data)
