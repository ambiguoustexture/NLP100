# Author：ambiguoustexture
# Date: 2020-03-08

import codecs
import numpy as np

file_features     = './features.txt'
file_theta        = './file_theta.npy'
file_encoding     = 'cp1252'

with codecs.open(file_features, 'r', file_encoding) as features:
    features = list(features)

theta = np.load(file_theta)
index_sorted = theta.argsort()
print('Top 10 features with high weight:')
for index in index_sorted[::-1][:10]:
    print('\t', theta[index], '\t', \
            features[index - 1].strip())

print('Top 10 features with low weight:')
for index in index_sorted[:10]:
    print('\t', theta[index], '\t', \
            features[index - 1].strip())
