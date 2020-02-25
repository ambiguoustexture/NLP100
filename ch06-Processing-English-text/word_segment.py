# Author：ambiguoustexture
# Date: 2020-02-25

from sentence_segment import sentence_segment

def word_segment(file):
    for sentence in sentence_segment(file):
        for word in sentence.split(' '):
            yield word.rstrip('.,;:?!')
        yield ''

if __name__ == '__main__':
    file = './nlp.txt'
    for word in word_segment(file):
        print(word)
