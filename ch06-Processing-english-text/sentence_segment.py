# Author：ambiguoustexture
# Date: 2020-02-25

import re

def sentence_segment(file):
    with open(file) as text:
        pattren = re.compile(r'''
                            (^.*? [\.|;|:|\?|!])        # (. or ; or : or ? or !)
                            \s                          # space
                            (A-Z).*                     # uppercase letters
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
        for line in text:
            line = line.strip()
            while len(line) > 0:
                match = pattren.match(line)
                if match:
                    yield match.group(1)
                    line = match.group(2)
                else:
                    yield line
                    line = ''

if __name__ == '__main__':
    file = './nlp.txt'
    for sentence in sentence_segment(file):
        print(sentence)
