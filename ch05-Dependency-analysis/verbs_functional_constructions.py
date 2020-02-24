# Author：ambiguoustexture
# Date: 2020-02-24

from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './verbs_functional_constructions.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)
    
    for sentence in sentences:
        for chunk in sentence:
            verbs = chunk.get_morphs_by_pos('動詞')
            
            if len(verbs) < 1:
                continue
            
            chunks_with_particle = []
            for src in chunk.srcs:
                if len(sentence[src].get_case_particle()) > 0:
                    chunks_with_particle.append(sentence[src])
            if len(chunks_with_particle) < 1:
                continue 
            
            sahen_wo_particle = ''
            for chunk_src in chunks_with_particle:
                sahen_wo_particle = chunk_src.get_sahen_wo_particle()
                if len(sahen_wo_particle) > 0:
                    chunk_need_remove = chunk_src
                    break
            if len(sahen_wo_particle) < 1:
                continue

            chunks_with_particle.remove(chunk_need_remove)
            chunks_with_particle.sort(key = lambda chunk: chunk.get_case_particle())

            text_result.write('{}\t{}\t{}\n'.\
                    format(\
                    sahen_wo_particle + verbs[0].base,\
                    ' '.join([chunk.get_case_particle() for chunk in chunks_with_particle]),\
                    ' '.join([chunk.get_chunk_string()  for chunk in chunks_with_particle])
                        ))
