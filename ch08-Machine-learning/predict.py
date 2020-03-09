# Author：ambiguoustexture
# Date: 2020-03-08

from learn import *

file_sentiment    = './sentiment.txt'
file_features     = './features.txt'
file_theta        = './file_theta.npy'
file_encoding     = 'cp1252'

sentence          = input('Please input a sentence > ')
features_dict     = load_features_dict(file_features, file_encoding)
data_one_x        = features_extract(sentence, features_dict)
theta             = np.load(file_theta)
h                 = hypothesis(data_one_x, theta)

if h > 0.5:
    print('label:+1', h)
else:
    print('label:-1', h)
