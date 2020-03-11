# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
from scipy import io

file_context_matrix_X_w2v = './context_matrix_X_w2v'
file_t_index_dict_w2v     = './t_index_dict_w2v'

with open(file_t_index_dict_w2v, 'rb') as t_index_dict_w2v:
    t_index_dict_w2v = pickle.load(t_index_dict_w2v)

file_context_matrix_X_w2v = io.loadmat(file_context_matrix_X_w2v)['context_matrix_X_w2v']
print(file_context_matrix_X_w2v[t_index_dict_w2v['United_States']])
