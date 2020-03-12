# Author: ambiguoustexture
# Date: 2020-03-12

import numpy as np

def evaluate(file_result):
    with open(file_result) as result:
        human_judgements = []
        model_judgements = []
        N = 0
        for line in result:
            cols = line.split('\t')
            human_judgements.append(float(cols[2]))
            model_judgements.append(float(cols[3]))
            N += 1

    human_judgements_sorted = np.argsort(human_judgements)
    model_judgements_sorted = np.argsort(model_judgements)

    human_judgements_order = [0] * N
    model_judgements_order = [0] * N

    for i in range(N):
        human_judgements_order[human_judgements_sorted[i]] = i
        model_judgements_order[model_judgements_sorted[i]] = i

    # calculate the Spearman's rank correlation coefficient
    sum = 0
    for i in range(N):
        sum += pow(human_judgements_order[i] - model_judgements_order[i], 2)
    spearman_coefficient = 1 - (6 * sum) / (N * (pow(N, 2) - 1))
    return spearman_coefficient

if __name__ == '__main__':
    file_result_w2v = './stuffs_94/result_w2v.tab'
    file_result_PC  = './stuffs_94/result_PC.tab'
    print('Spearman\'s rank correlation coefficient by word2vec:', evaluate(file_result_w2v))
    print('Spearman\'s rank correlation coefficient by context co-occurrence matrix:',
            evaluate(file_result_PC))
