# Author：ambiguoustexture
# Date: 2020-03-08

import random
import codecs

file_polarity_pos = './rt-polaritydata/rt-polarity.pos'
file_polarity_neg = './rt-polaritydata/rt-polarity.neg'
file_sentiment    = './sentiment.txt'
file_encoding     = 'cp1252'

res = []

with codecs.open(file_polarity_pos, 'r', file_encoding) as polarity_pos:
    res.extend(['+1 {}'.format(sentence.strip()) for sentence in polarity_pos])

with codecs.open(file_polarity_neg, 'r', file_encoding) as polarity_neg:
    res.extend(['-1 {}'.format(sentence.strip()) for sentence in polarity_neg])

random.shuffle(res)

with codecs.open(file_sentiment, 'w', file_encoding) as sentiment:
    print(*res, sep='\n', file=sentiment)

count_pos = 0
coutn_neg = 0
with codecs.open(file_sentiment, 'r', file_encoding) as sentiment:
    for sentence in sentiment:
        if sentence.startswith('+1'):
            count_pos += 1
        elif sentence.startswith('-1'):
            coutn_neg += 1

print('pos: ', count_pos, ' neg: ', coutn_neg)
