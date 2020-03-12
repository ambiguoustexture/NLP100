import pickle
from scipy import io

from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

file_t_index_dict = './stuffs_96/t_index_dict_countries'
file_matrix       = './stuffs_96/matrix_countries'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

matrix = io.loadmat(file_matrix)['matrix_countries']

t_sne = TSNE(learning_rate=500).fit_transform(matrix)

predictions = KMeans(n_clusters=5).fit_predict(matrix)

fig, ax = plt.subplots()
cmap = plt.get_cmap('Set1')
for index, label in enumerate(t_index_dict.keys()):
    cval = cmap(predictions[index] / 4)
    ax.scatter(t_sne[index, 0], t_sne[index, 1], marker='*', color=cval)
    ax.annotate(label, xy=(t_sne[index, 0], t_sne[index, 1]), color=cval)
plt.show()
