# Author: ambiguoustexture
# Date: 2020-03-11

from scipy import sparse, io
import sklearn.decomposition

file_context_matrix_X    = './context_matrix_X'
file_context_matrix_X_PC = './context_matrix_X_PC'

context_matrix_X = io.loadmat(file_context_matrix_X)['context_matrix_X']

context_matrix_X_PC = sklearn.decomposition.TruncatedSVD(300).fit_transform(context_matrix_X)
io.savemat(file_context_matrix_X_PC, {'context_matrix_X_PC': context_matrix_X_PC})

