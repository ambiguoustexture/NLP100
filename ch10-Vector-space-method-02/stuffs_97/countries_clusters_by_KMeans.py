# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
from scipy import io
from sklearn.cluster import KMeans

file_t_index_dict = './stuffs_96/t_index_dict_countries'
file_matrix       = './stuffs_96/matrix_countries'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

matrix = io.loadmat(file_matrix)['matrix_countries']

predictions = KMeans(n_clusters=5).fit_predict(matrix)

result = zip(t_index_dict.keys(), predictions)

for country, group in sorted(result, key=lambda x: x[1]):
    print('{}\t{}'.format(group, country))
