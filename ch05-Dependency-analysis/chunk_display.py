# Author：ambiguoustexture
# Date: 2020-02-23

from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'

with open(file_parsed) as text_parsed:
    sentences = chunk_analysis(text_parsed)
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                
                chunk_src = ''
                for morph in chunk.morphs:
                    chunk_src += morph.surface
                chunk_src = chunk_src.strip()
                chunk_dst = ''
                for morph in sentence[chunk.dst].morphs:
                    chunk_dst += morph.surface
                chunk_dst = chunk_dst.strip()
                if '。' in chunk_dst:
                    chunk_dst = chunk_dst[:-1]
                if chunk_dst != '' and chunk_src != '':
                    print('%s\t' % chunk_src, '%s' % chunk_dst)
