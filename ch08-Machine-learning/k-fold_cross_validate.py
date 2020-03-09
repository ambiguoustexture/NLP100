# Author: ambiguoustexture
# Date: 2020-03-09

import codecs
import snowballstemmer
import numpy as np

from learn import \
        init, load_features_dict, learn, features_extract, hypothesis
from accuracy_measure import score

def k_fold_cross_validate(k, file_data, file_features, file_result, 
        learn_rate, count_iteration):
    """
    k-fold cross validate.
    """
    with codecs.open(file_data, 'r', 'cp1252') as data, \
            open(file_result, 'w') as result:
        # get k parts of data
        data_all = list(data)
        data_divided = []
        unit = int(len(data_all) / k)
        for i in range(5):
            data_divided.append(data_all[i * unit : (i  + 1) * unit])
        # learn each part and validate use left parts
        for i in range(k):
            print(i + 1, '/', k)
            data_to_learn = []
            for j in range(k):
                if i == j:
                    data_to_validate = data_divided[j]
                else:
                    data_to_learn   += data_divided[j]

            features_dict = load_features_dict(file_features, 'cp1252')
            X, Y = init(data_to_learn, features_dict)
            theta = learn(X, Y, learn_rate, count_iteration)
            for sentence in data_to_validate:
                data_one_x = features_extract(sentence[3:], features_dict)
                h = hypothesis(data_one_x, theta)
                if h > 0.5:
                    result.write(sentence[0:2] + '\t+1\t' + str(h) + '\n')
                else:
                    result.write(sentence[0:2] + '\t-1\t' + str(h) + '\n')

if __name__ == '__main__':
    file_features  = './features.txt'
    file_sentiment = './sentiment.txt'
    file_result    = './k_fold_cross_validate_result.txt'
    learn_rate, count_iteration = 6.0, 1000

    k_fold_cross_validate(5, file_sentiment, file_features, file_result, 
            learn_rate, count_iteration)
    
    accuracy, precision, recall, f1 = score(file_result)
    print('Accuracy:'.ljust(14, ' '), accuracy)
    print('Precision:'.ljust(14, ' '), precision)
    print('Recall:'.ljust(14, ' '), recall)
    print('F1:'.ljust(14, ' '), f1)
