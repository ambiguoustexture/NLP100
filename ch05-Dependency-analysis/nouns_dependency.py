# Author：ambiguoustexture
# Date: 2020-02-24

from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './nouns_dependency.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)
    for sentence in sentences:
        index_nouns = [index for index in range(len(sentence))
                if len(sentence[index].get_morphs_by_pos('名詞')) > 0]
        if len(index_nouns) < 2:
            continue
        for index, index_x in enumerate(index_nouns[:-1]):
            for index_y in index_nouns[index + 1:]:
                flag_intersect  = False
                index_intersect = -1
                path = set()

                dst = sentence[index_x].dst
                while dst != -1:
                    if dst == index_y:
                        flag_intersect = True
                        break
                    path.add(dst)
                    dst = sentence[dst].dst

                if not flag_intersect:
                    dst = sentence[index_y].dst
                    while dst != -1:
                        if dst in path:
                            index_intersect = dst
                            break
                        else :
                            dst = sentence[dst].dst
                if index_intersect == -1:
                    text_result.write(sentence[index_x].get_original_surface('X'))
                    dst = sentence[index_x].dst
                    while dst != -1:
                        if dst == index_y:
                            text_result.write(' -> ' + sentence[dst].get_original_surface('Y', True))
                            break
                        else :
                            text_result.write(' -> ' + sentence[dst].get_chunk_string())
                        dst = sentence[dst].dst
                    text_result.write('\n')
                else :
                    text_result.write(sentence[index].get_original_surface('X'))
                    dst = sentence[index_x].dst
                    while dst != index_intersect:
                        text_result.write(' -> ' + sentence[dst].get_chunk_string())
                        dst = sentence[dst].dst
                    
                    text_result.write(' | ')
                    
                    text_result.write(sentence[index_y].get_original_surface('Y'))
                    dst = sentence[index_y].dst
                    while dst != index_intersect:
                        text_result.write(' -> ' + sentence[dst].get_chunk_string())
                        dst = sentence[dst].dst
                    text_result.write(' | ')

                    text_result.write(sentence[index_intersect].get_chunk_string())
                    text_result.write('\n')
