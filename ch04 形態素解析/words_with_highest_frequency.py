# Author：ambiguoustexture
# Date: 2020-02-13

from collections import Counter
from morphological_analysis import morphology_map

file_parsed = "./neko.txt.mecab"
words = morphology_map(file_parsed)

word_count = Counter()
word_count.update([word['surface'] for word in words])

items = word_count.most_common()
for item in items:
    print(item)

