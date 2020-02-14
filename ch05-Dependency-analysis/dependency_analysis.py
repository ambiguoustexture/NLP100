# Author：ambiguoustexture
# Date: 2020-02-14

import CaboCha

def dependency_analysis():
    with open(file) as text, open(file_parsed, 'w') as text_parsed:
        cabocha = CaboCha.Parser()
        for line in text:
            text_parsed.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

class Chunk:
    def __init__(self, sentence, morphs, dst, srcs):
        self.sentence = sentence
        self.morphs = morphs
        self.dst    = dst
        self.srcs   = srcs

if __name__ == '__main__':
    file = './neko.txt'
    file_parsed = './neko.txt.cabocha'
    dependency_analysis()
    
    sentences = []
    sentence  = []
    with open('neko.txt.cabocha') as text_parsed:
        for line in text_parsed:
            if line[0] == "*" :
                next
            if "\t" in line:
                item = line.strip().split("\t")
                try:
                    surf = item[0]
                    items = item[1].split(",")
                except IndexError:
                    next
                if not item == ['記号,空白,*,*,*,*,\u3000,\u3000,']:
                    sentence.append(Morph(surf, items[6], items[0], items[1]))
            elif "EOS" in line:
                if len(sentence) > 0:
                    sentences.append(sentence)
                sentence = []

    for morpheme in sentences[3]:
        print ('surface=%s\tbase=%s\tpos=%s\tpos1=%s' % (morpheme.surface, morpheme.base, morpheme.pos, morpheme.pos1))

