# Author：ambiguoustexture
# Date: 2020-02-23

from chunk_analysis import chunk_analysis
import CaboCha
import pydotplus as pydot

file_parsed = './sentence_input.txt.cabocha'
with open(file_parsed, mode='w') as sentence_parsed:
    cabocha = CaboCha.Parser()
    sentence_parsed.write(cabocha.parse(input('Please input a sentence --> ')).\
            toString(CaboCha.FORMAT_LATTICE))

with open(file_parsed) as text_parsed:
    sentences = chunk_analysis(text_parsed)
    for sentence in sentences:
        edges = []
        for index, chunk in enumerate(sentence):
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
                if chunk_src != '' and chunk_dst != '':
                    edges.append(((index, chunk_src), (chunk.dst, chunk_dst)))
    
        if len(edges) > 0:
            tree = pydot.graph_from_edges(edges, directed=True)
            tree.write_png('./dependency_visualization.png')
