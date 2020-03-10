# Author: ambiguoustexture
# Date: 2020-03-10

import math
import pickle
from collections import Counter
from collections import OrderedDict
from scipy import sparse, io

file_tc_counter       = './tc_counter'
file_t_counter        = './t_counter'
file_c_counter        = './c_counter'
file_context_matrix_X = './context_matrix_X'
file_t_index_dict     = './t_index_dict'

N = 68031841
with open(file_tc_counter, 'rb') as tc:
    tc_counter = pickle.load(tc)
with open(file_t_counter,  'rb') as t:
    t_counter  = pickle.load(t)
with open(file_c_counter,  'rb') as c:
    c_counter  = pickle.load(c)

t_index_dict = OrderedDict((key, i) for i, key in enumerate(t_counter.keys()))
c_index_dict = OrderedDict((key, i) for i, key in enumerate(c_counter.keys()))

t_size, c_size = len(t_index_dict), len(c_index_dict)
context_matrix_X = sparse.lil_matrix((t_size, c_size))

for tc, f_tc in tc_counter.items():
    if f_tc > 10:
        words = tc.split('\t')
        t, c = words[0], words[1]
        ppmi = max(math.log((N * f_tc) / (t_counter[t] * c_counter[c])), 0)
        context_matrix_X[t_index_dict[t], c_index_dict[c]] = ppmi

io.savemat(file_context_matrix_X, {'context_matrix_X': context_matrix_X})

with open(file_t_index_dict, 'wb') as t_index:
    pickle.dump(t_index_dict, t_index)
