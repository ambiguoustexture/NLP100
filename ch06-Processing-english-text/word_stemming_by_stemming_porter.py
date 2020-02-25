# Author：ambiguoustexture
# Date: 2020-02-25

from stemming.porter import stem 

file = './words.txt'
with open(file) as words:
    for word in words:
        print('%s\t' % word.rstrip(), '%s' % stem(word.rstrip()))
