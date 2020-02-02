# Author：ambiguoustexture
# Date: 2020-02-02
import re

def sequence_to_words(sequence):
    """clean the given sequence
    :param sequence:    given sequence (string, list, etc.)
    :return:            words in the sequence
    """
    sequence = re.sub('\n+', ' ', sequence).lower()
    words = re.split('\W+', sequence)
    
    return words

def get_n_gram(sequence, n, key):
    """naive implement of n-gram based on word or letter
    :param sequence:    given sequence (string, list, etc.)
    :param n:           n-gram for n=2
    :param key:         switch word based or letter based
                        "key = word" for word based
                        "key = letter" for letter based
    :return:            n-gram dictionary
    """
    words = sequence_to_words(sequence)
    if key == "word":
        n_gram_dic = {}
        for i in range(len(words) - n + 1):
            n_gram_current = " ".join(words[i:i + n])
            if n_gram_current not in n_gram_dic:
                n_gram_dic[n_gram_current] = 1 
            else:
                n_gram_dic[n_gram_current] += 1
    
    elif key == "letter":
        str = ''.join(words)
        n_gram_dic = {}
        for i in range(len(str) - n + 1):
            n_gram_current = str[i:i + n]
            if n_gram_current not in n_gram_dic:
                n_gram_dic[n_gram_current] = 1
            else:
                n_gram_dic[n_gram_current] += 1
    
    return n_gram_dic 

if __name__ == "__main__":
    # sequence = open("poem.txt").read()
    sequence = "I am an NLPer"
    bi_gram_word_based = get_n_gram(sequence, 2, key = "word")
    bi_gram_letter_based = get_n_gram(sequence, 2, key = "letter")
    print("Sentence: I am an NLPer")
    print("Word based bi-gram of the sentence is:\n" + str(bi_gram_word_based))
    print("letter based bi-gram of the sentence is\n:" + str(bi_gram_letter_based))
