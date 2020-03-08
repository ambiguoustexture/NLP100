# Author：ambiguoustexture
# Date: 2020-03-08

import codecs
import snowballstemmer
from collections import Counter
from stop_words import isStopword

file_sentiment    = './sentiment.txt'
file_features     = './features.txt'
file_encoding     = 'cp1252'

stemmer = snowballstemmer.stemmer('english')
word_counter = Counter()

with codecs.open(file_sentiment, 'r', file_encoding) as sentiment:
    for sentence in sentiment:
        for word in sentence[3:].split(' '):
            word = word.strip()
            word = stemmer.stemWord(word)
            if isStopword(word):
                continue
            if word != '!' and word != '?' and len(word) <= 1:
                continue
            word_counter.update([word])

# Use those with 6 or more appearances for features
features = [word for word, count in word_counter.items() if count >= 6]

with codecs.open(file_features, 'w', file_encoding) as content_features:
    print(*features, sep='\n', file=content_features)
