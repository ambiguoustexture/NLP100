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
    file_context_matrix_X_PC = './context_matrix_X_PC'
    file_t_index_dict        = './t_index_dict'

    with open(file_t_index_dict, 'rb') as t_index_dict:
        t_index_dict = pickle.load(t_index_dict)

    context_matrix_X_PC = io.loadmat(file_context_matrix_X_PC)['context_matrix_X_PC']
    word_a = context_matrix_X_PC[t_index_dict['United_States']]
    word_b = context_matrix_X_PC[t_index_dict['U.S']]

    print('Cosine similarity between "United_States" and "U.S":', sim_cos(word_a, word_b))
