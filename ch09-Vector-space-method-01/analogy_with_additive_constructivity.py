# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
import numpy as np 
from scipy import io
from similarity_cosine import sim_cos 

file_context_matrix_X_PC = './context_matrix_X_PC'
file_t_index_dict        = './t_index_dict'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

context_matrix_X_PC = io.loadmat(file_context_matrix_X_PC)['context_matrix_X_PC']

words_additive = context_matrix_X_PC[t_index_dict['Spain']] \
        - context_matrix_X_PC[t_index_dict['Madrid']] \
        + context_matrix_X_PC[t_index_dict['Athens']]
words_similarities = [sim_cos(words_additive, context_matrix_X_PC[i])
        for i in range(len(t_index_dict))]
words_similarities_sorted = np.argsort(words_similarities)
words = list(t_index_dict.keys())

for index in words_similarities_sorted[:-11:-1]:
    print(words[index].ljust(14, ' '), words_similarities[index])    
