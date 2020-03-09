# Author：ambiguoustexture
# Date: 2020-03-09

import codecs
import snowballstemmer
import numpy as np
from stop_words import isStopword
from learn import hypothesis, features_extract, load_features_dict

file_sentiment    = './sentiment.txt'
file_features     = './features.txt'
file_theta        = './file_theta.npy'
file_result       = './labeling_result.txt'
file_encoding     = 'cp1252'

stemmer = snowballstemmer.stemmer('english')
features_dict = load_features_dict(file_features, file_encoding)
theta = np.load(file_theta)

with codecs.open(file_sentiment, 'r', file_encoding) as sentiment, \
        open(file_result, 'w') as result:
    for sentence in sentiment:
        data_one_x = features_extract(sentence[3:], features_dict)
        h = hypothesis(data_one_x, theta)
        if h > 0.5:
            result.write(sentence[0:2] + '\t+1\t' + str(h) + '\n')
        else :
            result.write(sentence[0:2] + '\t-1\t' + str(h) + '\n')
        
