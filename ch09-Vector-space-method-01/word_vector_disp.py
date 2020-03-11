# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
from scipy import io

file_context_matrix_X_PC = './context_matrix_X_PC'
file_t_index_dict        = './t_index_dict'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

context_matrix_X_PC = io.loadmat(file_context_matrix_X_PC)['context_matrix_X_PC']
print(context_matrix_X_PC[t_index_dict['United_States']])
