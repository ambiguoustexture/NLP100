# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
import numpy as np 
from scipy import io

def sim_cos(word_a, word_b):
    """
    calculate the cosine similarity
    """
    mul_ab = np.linalg.norm(word_a) * np.linalg.norm(word_b)
    if mul_ab == 0:
        return -1
    else:
        return np.dot(word_a, word_b) / mul_ab

if __name__ == '__main__':
    file_context_matrix_X_w2v = './context_matrix_X_w2v'
    file_t_index_dict_w2v     = './t_index_dict_w2v'

    with open(file_t_index_dict_w2v, 'rb') as t_index_dict_w2v:
        t_index_dict_w2v = pickle.load(t_index_dict_w2v)

    context_matrix_X_w2v = io.loadmat(file_context_matrix_X_w2v)['context_matrix_X_w2v']
    word_a = context_matrix_X_w2v[t_index_dict_w2v['United_States']]
    word_b = context_matrix_X_w2v[t_index_dict_w2v['U.S']]

    print('Cosine similarity between "United_States" and "U.S":', sim_cos(word_a, word_b))
