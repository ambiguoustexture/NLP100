# Author: ambiguoustexture
# Date: 2020-03-12

import pickle
from scipy import io

from similarity_cosine import sim_cos 

def similarity_bt_cols(file_t_index_dict, file_matrix, file_analogy_data, file_result):
    with open(file_t_index_dict, 'rb') as t_index_dict:
        t_index_dict = pickle.load(t_index_dict)

    try:
        matrix = io.loadmat(file_matrix)['matrix_w2v']
    except:
        matrix = io.loadmat(file_matrix)['context_matrix_X_PC']

    with open(file_analogy_data) as analogy_data, \
            open(file_result, 'wt') as result:
        flag_header = True
        for line in analogy_data:
            if flag_header:
                flag_header = False
                continue
            cols = line.split('\t')
            try:
                similarity = sim_cos(matrix[t_index_dict[cols[0]]],
                        matrix[t_index_dict[cols[1]]])
            except KeyError:
                similarity = -1
            print('{}\t{}'.format(line.strip(), similarity), file=result)

if __name__ == '__main__':
    file_matrix_w2v       = '../stuffs_90/matrix_w2v'
    file_matrix_PC        = '../../ch09-Vector-space-method-01/context_matrix_X_PC'
    file_t_index_dict_w2v = '../stuffs_90/t_index_dict_w2v'
    file_t_index_dict_PC  = '../../ch09-Vector-space-method-01/t_index_dict'
    file_analogy_data     = './wordsim353/combined.tab'
    file_result_w2v       = './result_w2v.tab'
    file_result_PC        = './result_PC.tab'
    
    similarity_bt_cols(file_t_index_dict_w2v, file_matrix_w2v, file_analogy_data, file_result_w2v)
    
    similarity_bt_cols(file_t_index_dict_PC,  file_matrix_PC,  file_analogy_data, file_result_PC)
    
