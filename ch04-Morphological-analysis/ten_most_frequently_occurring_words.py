# Author：ambiguoustexture
# Date: 2020-02-13

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from collections import Counter
from morphological_analysis import morphology_map

file_parsed = "./neko.txt.mecab"
words = morphology_map(file_parsed)
words_without_punctuation = []
for word in words:
    if word['pos'] != '記号':
        words_without_punctuation.append(word)

word_count = Counter()
word_count.update([word['surface'] for word in words_without_punctuation])

size   = 10
items  = word_count.most_common(size)
items  = list(zip(*items))
words  = items[0]
counts = items[1]

fig = plt.figure(figsize=(8, 6))

fp = FontProperties(fname=r'./MS-Mincho.ttf', size=14)
plt.bar(range(0, size), counts, align='center', alpha=0.4)
plt.xticks(range(0, size))
plt.xlabel(words, fontproperties=fp)
plt.ylabel('Frequency')
plt.title('Top 10 frequent words')
plt.show()
