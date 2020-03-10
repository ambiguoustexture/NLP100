# Author：ambiguoustexture
# Date: 2020-03-10

file_shaped    = './enwiki-20150112-400-r100-10576_shaped.txt'
file_countries = './countries.txt'
file_compound_words = './compound_words_process_result.txt'

countries_set  = set()
countries_dict = {}
with open(file_countries) as countries:
    for country in countries:
        words = country.split(' ')
        if len(words) > 1:
            countries_set.add(country.strip())
            if words[0] in countries_dict:
                compound_len = countries_dict[words[0]]
                if not len(words) in compound_len:
                    compound_len.append(len(words))
                    compound_len.sort(reverse=True)
            else:
                countries_dict[words[0]] = [len(words)]

with open(file_shaped) as text_shaped, \
        open(file_compound_words, 'w') as compound_words:
    for line in text_shaped:
        words = line.strip().split(' ')
        res = []
        flag_skip = 0
        for i in range(len(words)):
            if flag_skip > 0:
                flag_skip -= 1
                continue
            if words[i] in countries_dict:
                flag_hit = False
                for length in countries_dict[words[i]]:
                    if ' '.join(words[i:i + length]) in countries_set:
                        res.append('_'.join(words[i:i+length]))
                        flag_skip = length - 1
                        flag_hit = True
                        break
                if flag_hit:
                    continue
            res.append(words[i])
        print(*res, sep=' ', end='\n', file=compound_words)
