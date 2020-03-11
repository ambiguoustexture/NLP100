# Author: ambiguoustexture
# Date: 2020-03-11

file_analogy_data        = './questions-words.txt'
file_analogy_data_family = './questions-words_family.txt'

with open(file_analogy_data) as analogy_data, \
        open(file_analogy_data_family, 'w') as analogy_data_family:
    flag_target = False
    for line in analogy_data:
        if flag_target:
            if line.startswith(': '):
                break
            print(line.strip(), file=analogy_data_family)
        elif line.startswith(': family'):
            flag_target = True
