# Author：ambiguoustexture
# Date:   2020-02-02

import random

def typoglycemia(sequence):
    """
    Function that leaves the characters at the beginning and end of each word, 
    and rearranges the order of the other characters randomly. 
    However, words with a length of 4 or less are not rearranged.
    :param sequence:    given text
    :return:            rearranged text
    """
    words = sequence.split()
	
    for i in range(len(words)):
        if len(words[i]) > 4:
            word_partial = list(words[i][1:-1])
            random.shuffle(word_partial)
            word_shuffle = "".join(word_partial)
            words[i] = words[i][0] + word_shuffle + words[i][-1]
    
    return ' '.join(words[:-1]) + words[-1]

if __name__ == "__main__":
    sequence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(sequence))

