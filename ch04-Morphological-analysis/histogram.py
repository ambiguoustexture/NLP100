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

items  = word_count.most_common()
items  = list(zip(*items))
counts = items[1]

fig = plt.figure()
# fp = FontProperties(fname=r'./MS-Mincho.ttf', size=14)
plt.hist(counts, bins=20, range=(1, 20))
plt.xlabel('frequency of words')
plt.ylabel('Frequency')
plt.xlim(xmin=1, xmax=20)
plt.title('Histogram of word count')
plt.show()
