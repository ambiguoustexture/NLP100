# Author: ambiguoustexture
# Date: 2020-03-12

import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

file_t_index_dict = './stuffs_90/t_index_dict_w2v'
file_matrix       = './stuffs_90/matrix_w2v'
file_countries    = '../ch09-Vector-space-method-01/countries.txt'

file_t_index_dict_countries = './t_index_dict_countries'
file_matrix_countries       = './matrix_countries'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

matrix = io.loadmat(file_matrix)['matrix_w2v']

t_index_dict_countries = OrderedDict()
matrix_countries = np.empty([0, 300], dtype=np.float64)
count = 0

with open(file_countries) as countries:
    for country in countries:
        try:
            country = country.strip().replace(' ', '_')
            index = t_index_dict[country]
            matrix_countries = np.vstack([matrix_countries, matrix[index]])
            t_index_dict_countries[country] = [count]
            count += 1
        except:
            pass

io.savemat(file_matrix_countries, {'matrix_countries':matrix_countries})
with open(file_t_index_dict_countries, 'wb') as t_index:
    pickle.dump(t_index_dict_countries, t_index)
