# Author：ambiguoustexture
# Date: 2020-02-13

from morphological_analysis import morphology_map

file_parsed = "./neko.txt.mecab"

items_list = []

words = morphology_map(file_parsed)

nouns = []
for word in words:
    if word['pos'] == '名詞':
        nouns.append(word['surface'])
    else:
        if len(nouns) > 1:
            items_list.append("".join(nouns))
        nouns = []

items = set(items_list)
items = sorted(items, key=items_list.index)
for item in items:
    print(item)
