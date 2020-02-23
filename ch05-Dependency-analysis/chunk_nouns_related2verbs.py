# Author：ambiguoustexture
# Date: 2020-02-23

from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'

with open(file_parsed) as text_parsed:
    sentences = chunk_analysis(text_parsed)
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                
                flag_nouns = False
                for morph in chunk.morphs:
                    if morph.pos == '名詞':
                        flag_nouns = True
                chunk_nouns = ''
                if flag_nouns:
                    for morph in chunk.morphs:
                        chunk_nouns += morph.surface
                    chunk_nouns = chunk_nouns.strip()
                    if chunk_nouns[-1] == '、':
                        chunk_nouns = chunk_nouns[:-1]
                    
                    flag_verbs = False
                    for morph in sentence[chunk.dst].morphs:
                        if morph.pos == '動詞':
                            flag_verbs = True
                    chunk_verbs = ''
                    if flag_verbs:
                        for morph in sentence[chunk.dst].morphs:
                            chunk_verbs += morph.surface 
                        if chunk_verbs[-1] == '。' or chunk_verbs[-1] == '、':
                            chunk_verbs = chunk_verbs[:-1]
                        print('%s\t' % chunk_nouns, '%s' % chunk_verbs)
                            
              
