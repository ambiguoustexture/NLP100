# Author：ambiguoustexture
# Date: 2020-02-14

import CaboCha

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

def morpheme_analysis(file_parsed):
    sentence, sentences = [], []
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
    return sentences

if __name__ == '__main__':
    file_raw, file_parsed = './neko.txt', './neko.txt.cabocha'
    with open(file_raw) as text, open(file_parsed, 'w') as text_parsed:
        cabocha = CaboCha.Parser()
        for line in text:
            text_parsed.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))
    
    sentences = morpheme_analysis(file_parsed)
    for morph in sentences[3]:
        print('surface: ',  morph.surface.ljust(4, chr(12288)),\
                '\tbase: ', morph.base.ljust(4, chr(12288)),\
                '\tpos: ' , morph.pos.ljust(4, chr(12288)),\
                '\tpos1: ', morph.pos1.ljust(4, chr(12288)))
