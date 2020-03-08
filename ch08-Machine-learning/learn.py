# Author：ambiguoustexture
# Date: 2020-03-08

import codecs
import snowballstemmer
import numpy as np
from stop_words import isStopword

def hypothesis(X, theta):
    """
    for X, predict Y using theta
    """
    return 1.0 / (1.0 + np.exp(-X.dot(theta)))

def cost(X, Y, theta):
    """
    calculate difference between predicted result and correct answer Y for X
    """
    m = Y.size
    h = hypothesis(X, theta)
    j = 1 / m * np.sum(-Y * np.log(h) - \
            (np.ones(m) - Y) * np.log(np.ones(m) - h))
    return j

def gradient(X, Y, theta):
    """
    calculate the gradient
    """
    m = Y.size
    h = hypothesis(X, theta)
    grad = 1 / m * (h - Y).dot((X))
    return grad 

def load_features_dict(file_features):
    """
    load features from file_features 
    """
    with codecs.open(file_features, 'r', file_encoding) as features:
        return {sentence.strip(): i for i, sentence in enumerate(features, start=1)}

def features_extract(sentence, features_dict):
    """
    extract the features contained in features_dict from the sentence
    """
    data_one_x = np.zeros(len(features_dict) + 1, dtype=np.float64)
    data_one_x[0] = 1
    stemmer = snowballstemmer.stemmer('english')
    for word in sentence.split(' '):
        word = word.strip()
        if isStopword(word):
            continue
        word = stemmer.stemWord(word)
        try:
            data_one_x[features_dict[word]] = 1
        except:
            pass
    return data_one_x

def init(sentiment_list, features_dict):
    """
    create matrices for learning and matrices of polarity labels from correct answer data sentiments
    """
    X = np.zeros([len(sentiment_list), len(features_dict) + 1], dtype=np.float64)
    Y = np.zeros(len(sentiment_list), dtype=np.float64)
    for i, sentence in enumerate(sentiment_list):
        X[i] = features_extract(sentence[3:], features_dict)
        if sentence[0:2] == '+1':
            Y[i] = 1
    return X, Y

def learn(X, Y, learn_rate, count_iteration):
    """
    learning logistic regression
    """
    theta = np.zeros(X.shape[1])
    cost_current = cost(X, Y, theta)
    print('Start learning', '\t\tcost:', cost_current)
    for i in range(1, count_iteration + 1):
        grad   = gradient(X, Y, theta)
        theta -= learn_rate * grad
        if i % 100 == 0:
            cost_current  = cost(X, Y, theta)
            print('\tLearning:', i, '\tcost:', cost_current)
    cost_current = cost(X, Y, theta)
    print('End learning', '\t\tcost:', cost_current)
    return theta

if __name__ == '__main__':
    file_sentiment    = './sentiment.txt'
    file_features     = './features.txt'
    file_theta        = './file_theta.npy'
    file_encoding     = 'cp1252'

    features_dict = load_features_dict(file_features)
    with codecs.open(file_sentiment, 'r', file_encoding) as sentiment:
        X, Y = init(list(sentiment), features_dict)
    
    learn_rate      = 6.0
    count_iteration = 1000
    print('Learn rate:', learn_rate, '\tNumber of learning iterations:', count_iteration)
    theta = learn(X, Y, learn_rate, count_iteration)
    np.save(file_theta, theta)
