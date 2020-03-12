# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

file_t_index_dict = './stuffs_96/t_index_dict_countries'
file_matrix       = './stuffs_96/matrix_countries'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

matrix = io.loadmat(file_matrix)['matrix_countries']

ward = ward(matrix)

dendrogram(ward, labels=list(t_index_dict.keys()), leaf_font_size=8, orientation='left')
plt.show()
