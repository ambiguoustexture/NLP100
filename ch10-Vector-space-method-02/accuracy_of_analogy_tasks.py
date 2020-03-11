# Author: ambiguoustexture
# Date: 2020-03-11

file_result_w2v = './stuffs_92/result_w2v.txt'
file_result_PC  = './stuffs_92/result_PC.txt'

with open(file_result_w2v) as result_w2v:
    count, total = 0, 0
    for line in result_w2v:
        cols = line.split(' ')
        total += 1
        if cols[3] == cols[4]:
            count += 1
    print('Accuracy of word2vec model:', count / total)

with open(file_result_PC)  as result_PC:
    count, total = 0, 0
    for line in result_PC:
        cols = line.split(' ')
        total += 1
        if cols[3] == cols[4]:
            count += 1
    print('Accuracy of PCA model:', count / total)
