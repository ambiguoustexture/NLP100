# Author：ambiguoustexture
# Date: 2020-03-10

file_original = './enwiki-20150112-400-r100-10576.txt'
file_shaped   = './enwiki-20150112-400-r100-10576_shaped.txt'

with open(file_original) as text_original, \
        open(file_shaped, 'wt') as text_shaped:
    for line in text_original:
        words = []
        for word in line.split(' '):
            word = word.strip().strip('.,!?;:()[]\'"')
            if word != '':
                words.append(word)
        print(*words, sep=' ', end='\n', file=text_shaped)
