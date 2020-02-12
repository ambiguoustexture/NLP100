# Author：ambiguoustexture
# Date: 2020-02-13

from morphological_analysis import morphology_map

file_parsed = "./neko.txt.mecab"

verbs = set()
verbs_order = []

words = morphology_map(file_parsed)
for word in words:
    if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
        verbs.add(word['surface'])
        verbs_order.append(word['surface'])

items = sorted(verbs, key=verbs_order.index)
for item in items:
    print(item)
