# Author：ambiguoustexture
# Date: 2020-02-13

from morphological_analysis import morphology_map

file_parsed = "./neko.txt.mecab"

items = set()
items_order = []

words = morphology_map(file_parsed)
for word in words:
    if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
        items.add(word['surface'])
        items_order.append(word['surface'])

items = sorted(items, key=items_order.index)
for item in items:
    print(item)
