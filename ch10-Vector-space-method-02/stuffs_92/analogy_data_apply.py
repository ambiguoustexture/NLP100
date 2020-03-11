# Author: ambiguoustexture
# Date: 2020-03-11

import time
import pickle
from scipy import io
from similarity_cosine_w2v import sim_cos

def find_max_similarity(file_matrix, file_t_index_dict, file_analogy_data, file_result):
    # load matrix
    try:
        matrix = io.loadmat(file_matrix)['matrix_w2v']
    except:
        matrix = io.loadmat(file_matrix)['context_matrix_X_PC']
    # load t_index_dict
    with open(file_t_index_dict, 'rb') as t_index_dict:
        t_index_dict = pickle.load(t_index_dict)
        keys = list(t_index_dict.keys())
    # find each max_similarity
    with open(file_analogy_data) as analogy_data, \
            open(file_result, 'wt') as result:
        for line in analogy_data:
            cols = line.split(' ')
            try:
                vec_additive = matrix[t_index_dict[cols[1]]] \
	                         - matrix[t_index_dict[cols[0]]] \
	                         + matrix[t_index_dict[cols[2]]]
                max_similarity, max_index, max_result = -1, 0, ''
                for index in range(len(t_index_dict)):
                    similarity = sim_cos(vec_additive, matrix[index])
                    if similarity > max_similarity:
                        max_index = index
                        max_similarity = similarity
                        max_result = keys[max_index]
            except KeyError:
                max_similarity = -1
                max_result     = ''
            print('{} {} {}'.format(line.strip(), max_result, max_similarity), file=result)

if __name__ == '__main__':
    file_matrix_w2v          = '../stuffs_90/matrix_w2v.mat'
    file_matrix_PC           = '../../ch09-Vector-space-method-01/context_matrix_X_PC'
    file_t_index_dict_w2v    = '../stuffs_90/t_index_dict_w2v'
    file_t_index_dict_PC     = '../../ch09-Vector-space-method-01/t_index_dict'
    file_analogy_data        = '../stuffs_91/questions-words_family.txt'
    file_result_by_w2v       = './result_w2v.txt'
    file_result_by_PC        = './result_PC.txt'
    
    time_start = time.time()
    find_max_similarity(file_matrix_w2v, file_t_index_dict_w2v, file_analogy_data, file_result_by_w2v)
    time_end   = time.time()
    print('With matrix from 90, cost', time_end - time_start, 's.')
    
    time_start = time.time()
    find_max_similarity(file_matrix_PC,  file_t_index_dict_PC, file_analogy_data, file_result_by_PC)
    time_end   = time.time()
    print('With matrix from 85, cost', time_end - time_start, 's.')
