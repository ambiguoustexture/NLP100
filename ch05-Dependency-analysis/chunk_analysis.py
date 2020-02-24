# Author：ambiguoustexture
# Date: 2020-02-22

import morph_analysis 

class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst    = -1
        self.srcs   = []

    def get_morphs_by_pos(self, pos, pos1=''):
        if len(pos1) > 0:
            return [res for res in self.morphs
                    if (res.pos == pos) and (res.pos1 == pos1)]
        else:
            return [res for res in self.morphs if res.pos == pos]

    def get_case_particle(self):
        # used in 45
        particles = self.get_morphs_by_pos('助詞')
        if len(particles) > 1:
            case_particles = self.get_morphs_by_pos('助詞', '格助詞')
            if len(case_particles) > 0:
                particles = case_particles
        if len(particles) > 0:
            return particles[-1].surface
        else :
            return ''

    def get_chunk_string(self):
        # used in 46
        str = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                str += morph.surface
        return str
    
    def get_sahen_wo_particle(self):
        # used in 47
        for index, morph in enumerate(self.morphs[0:-1]):
            if morph.pos == '名詞' and (morph.pos1 == 'サ変接続')\
                    and (self.morphs[index + 1].pos == '助詞')\
                    and (self.morphs[index + 1].surface == 'を'):
                return morph.surface + self.morphs[index + 1].surface 
        return ''

def chunk_analysis(file_parsed):
    sentences = []
    sentence = []
    for line in file_parsed:
        if line == "EOS\n":
            for index, chunk in enumerate(sentence[:-1]):
                if chunk.dst != -1:
                    sentence[chunk.dst].srcs.append(index)
            sentences.append(sentence)
            sentence = []
        elif line[0] == "*":
            chunk = Chunk()
            chunk.dst = int(line.split()[2].strip("D"))
            sentence.append(chunk)
        else:
            surface = line.split('\t')[0]
            others = line.split('\t')[1].split(",")
            base, pos, pos1 = others[6], others[0], others[1]
            morph = morph_analysis.Morph(surface, base, pos, pos1)
            sentence[-1].morphs.append(morph)
    return sentences


if __name__ == "__main__":
    file_parsed = './neko.txt.cabocha'
    with open("neko.txt.cabocha", "r") as text_parsed:
        sentences = chunk_analysis(text_parsed)
        # index of the 8th sentence is 10 in fact
        for index, chunk_current in enumerate(sentences[10]):
            chunk_string = ''
            for morph in chunk_current.morphs:
                chunk_string += morph.surface
            print('chunk: ', chunk_string.ljust(8, chr(12288)),\
                    '\tdst: %2d ' % chunk_current.dst,\
                    '\tsrcs: ',chunk_current.srcs)
