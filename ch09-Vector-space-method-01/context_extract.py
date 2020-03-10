# Author: ambiguoustexture
# Date: 2020-03-10

import random

file_compound_words = './compound_words_process_result.txt'
file_context        = './context.txt'

with open(file_compound_words) as compound_words, \
        open(file_context, 'w') as context:
    for index, line in enumerate(compound_words):
        words = line.strip().split(' ')
        for j in range(len(words)):
            t = words[j]
            d = random.randint(1, 5)
            for k in range(max(j - d, 0), min(j + d + 1, len(words))):
                if j != k:
                    print('{}\t{}'.format(t, words[k]), file=context)
