# Author：ambiguoustexture
# Date: 2020-02-24

from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './nouns2root.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)
    
    for sentence in sentences:
        for chunk in sentence:
            if len(chunk.get_morphs_by_pos('名詞')) > 0:
                if chunk.get_chunk_string() != '':
                    text_result.write(chunk.get_chunk_string())

                dst = chunk.dst
                while dst != -1:
                    text_result.write(' -> ' + sentence[dst].get_chunk_string())
                    dst = sentence[dst].dst
                text_result.write('\n')
