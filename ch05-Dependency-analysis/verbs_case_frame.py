# Author：ambiguoustexture
# Date: 2020-02-24

from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './verbs_case_frame.txt'

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
            
            chunks_with_particle.sort(key = lambda chunk: chunk.get_case_particle())

            text_result.write('{}\t{}\t{}\n'.\
                    format(\
                    verbs[0].base,\
                    ' '.join(chunk.get_case_particle() for chunk in chunks_with_particle),\
                    ' '.join(chunk.get_chunk_string()  for chunk in chunks_with_particle)
                        ))
