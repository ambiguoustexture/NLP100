## 第4章: 形態素解析
Morphological analysis<br/>
形态分析

夏目漱石の小説『吾輩は猫である』の文章
（[neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．<br/>
Morphologically analyze the text([neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)) 
of Soseki Natsume's novel "I am a cat" using MeCab, 
and save the results in a file called neko.txt.mecab. 
Use this file to implement a program that addresses the following questions.<br/>
使用MeCab对夏目漱石的小说“我是猫”的文本
（[neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)）进行形态分析，
并将结果保存在名为neko.txt.mecab的文件中。 使用此文件实现解决以下问题的程序：

なお，問題37, 38, 39は[matplotlib](http://matplotlib.org/)もしくは[Gnuplot](http://www.gnuplot.info/)を用いるとよい．<br/>
For problems 37, 38, and 39, use [matplotlib](http://matplotlib.org/) 
or [Gnuplot](http://www.gnuplot.info/).<br/>
对于步骤37、38和39，使用[matplotlib](http://matplotlib.org/)
或[Gnuplot](http://www.gnuplot.info/)。

### 30. 形態素解析結果の読み込み
Read morphological analysis results<br/>
形態素解析結果の読み込み

形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），
基本形（base），品詞（pos），
品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．<br/>
Implement a program that reads the result of morphological analysis (neko.txt.mecab).
However, each morpheme is stored in a mapping type with the surface type (surface), 
basic type (base), part of speech (pos), 
and part of speech class 1 (pos1) as keys, 
and one sentence is represented as a list of morphemes (mapping type) Please.
Use the program you created here for the rest of Chapter 4.<br/>
实现一个程序，用以读取形态分析的结果（neko.txt.mecab）。 
另外，每个语素都以映射类型存储，其中以
表层类型（surface），
基本类型（base），词性（pos）和词性分类1（pos1）作为键值，
并且一个句子表示为一组语素（映射类型）。
将此处创建的程序用于第4章的其余部分。

```Python
import MeCab

def morphology_map(file_parsed):
    with open(file_parsed) as mecab_parsed:
        mecab_parsed = mecab_parsed.read()
    mecab_parsed = mecab_parsed.lstrip('\n')
    lines = mecab_parsed.splitlines()
    res = []

    for line in lines:
        line_current = line.replace('\t',',').split(',')
        if line_current[0] == 'EOS':
            break
        else:
            dict = {
                    'surface' :line_current[0],
                    'base'    :line_current[-3],
                    'pos'     :line_current[1],
                    'pos1'    :line_current[2]
                    }
            res.append(dict)
    return res

if __name__ == "__main__":
    file = './neko.txt'
    file_parsed = './neko.txt.mecab'

    with open(file) as text, open(file_parsed, 'w') as text_parsed:
        mecab_tagger = MeCab.Tagger()
        mecab_parsed = mecab_tagger.parse(text.read())
        text_parsed.write(mecab_parsed)

    res = morphology_map(file_parsed)
    for item in res:
        print(item)
```
```Shell
➜ python morphological_analysis.py > morphological_analysis.txt; head -4 morphological_analysis.txt
{'surface': '一', 'base': '一', 'pos': '名詞', 'pos1': '数'}
{'surface': '\u3000', 'base': '\u3000', 'pos': '記号', 'pos1': '空白'}
{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'}
{'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '係助詞'}
```
### 31. 動詞
verb<br/>
动词

動詞の表層形をすべて抽出せよ．<br/>
Extract all verb surface forms.<br/>
提取所有动词的表层形式。

```python
from morphological_analysis import morphology_map

file_parsed = "./neko.txt.mecab"

verbs = set()
verbs_order = []

words = morphology_map(file_parsed)
for word in words:
    if word['pos'] == '動詞':
        verbs.add(word['surface'])
        verbs_order.append(word['surface'])

verbs = sorted(verbs, key=verbs_order.index)
for verb in verbs:
    print(verb)
```
```Shell
➜ python verbs.py > verbs.txt; head -4 verbs.txt
生れ
つか
し
泣い
```

### 32. 動詞の原形
Verb form<br/>
动词原形

動詞の原形をすべて抽出せよ．<br/>
Extract all verb forms.<br/>
提取所有动词的原型。

```Python
words = morphology_map(file_parsed)
for word in words:
    if word['pos'] == '動詞':
        verbs.add(word['base'])
        verbs_order.append(word['base'])
```
```Shell
➜ python verbs_primitive.py > verbs_primitive.txt; head -4 verbs_primitive.txt
生れる
つく
する
泣く
```

### 33. サ変名詞
nouns which verbs can be formed by adding "する" to<br/>
可以通过后加“する”变成动词的名词

サ変接続の名詞をすべて抽出せよ．<br/>
Extract all nouns which verbs can be formed by adding "する" to.<br/>
提取所有可以通过后加“する”变成动词的名词。

```Python
words = morphology_map(file_parsed)
for word in words:
    if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
        items.add(word['surface'])
        items_order.append(word['surface'])
```
```Shell
➜ python nouns_suru.py > nouns_suru.txt; head -4 nouns_suru.txt
見当
記憶
話
装飾
```

### 34. 「AのB」

2つの名詞が「の」で連結されている名詞句を抽出せよ．<br/>
Extract a noun phrase where two nouns are connected by "の".<br/>
提取由“の”连接的名词词组

```Python
items_list = []
words = morphology_map(file_parsed)
for i in range(1, len(words) - 1):
    if words[i]['surface'] == 'の' and words[i - 1]['pos'] == '名詞' and words[i + 1]['pos'] == '名詞':
            items_list.append(words[i - 1]['surface'] + 'の' + words[i + 1]['surface'])

items = set(items_list)
items = sorted(items, key=items_list.index)
for item in items:
    print(item)
```
```Shell
➜ python nouns_connected_with_no.py > nouns_connected_with_no.txt; head -4 nouns_connected_with_no.txt
彼の掌
掌の上
書生の顔
はずの顔
```

### 35. 名詞の連接
Noun concatenation<br/>
名词串联

名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．<br/>
Extract the concatenation of nouns (nouns that appear consecutively) with the longest match.<br/>
提取最长的串联的名词词组

```Python
words = morphology_map(file_parsed)
nouns = []
for word in words:
    if word['pos'] == '名詞':
        nouns.append(word['surface'])
    else:
        if len(nouns) > 1:
            items_list.append("".join(nouns))
        nouns = []
```
```Shell
➜ python concatenation_longest.py > concatenation_longest.txt; head concatenation_longest.txt
人間中
一番獰悪
時妙
一毛
その後猫
一度
ぷうぷうと煙
邸内
三毛
書生以外
```

### 36. 単語の出現頻度
Occurrence of ward<br/>
词的出现频率

文章中に出現する単語とその出現頻度を求め，
出現頻度の高い順に並べよ．<br/>
Find the words that appear in the text and their frequency of occurrence, 
and arrange them in descending order of frequency of appearance.<br/>
找到出现在文本中的单词及其出现的频率，
并按照出现频率的降序排列它们。

```Python
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

items = word_count.most_common()
for item in items:
    print(item)
```
```Shell
➜ python words_with_highest_frequency.py > words_with_highest_frequency.txt; head words_with_highest_frequency.txt
('の', 9194)
('て', 6873)
('は', 6422)
('に', 6268)
('を', 6071)
('と', 5515)
('が', 5339)
('た', 3989)
('で', 3813)
('も', 2479)
```

### 37. 頻度上位10語
The 10 most frequently occurring words<br/>
词频最高的10个词

出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．<br/>
Display the 10 most frequently occurring words and their frequency of occurrence 
in a graph (eg a bar graph).<br/>
在图（例如条形图）中展示10个最频繁出现的单词及其出现频率。
![bar graph](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch04-Morphological-analysis/ten_most_frequently_occurring_words.png)

### 38. ヒストグラム
histogram<br/>
直方图

単語の出現頻度のヒストグラム
（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．<br/>
Draw a histogram of the frequency of occurrence of the word 
(the horizontal axis represents the frequency of appearance, 
and the vertical axis represents the number of types of words 
whose appearance frequency is represented by a bar graph).<br/>
绘制词频直方图
（横轴表示出现频率，纵轴表示出现频率以条形图表示的单词种数）。
![histrogram graph](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch04-Morphological-analysis/histogram.png)

### 39. Zipfの法則
Zipf's law<br/>
齐夫定律

単語の出現頻度順位を横軸，
その出現頻度を縦軸として，両対数グラフをプロットせよ．<br/>
Plot a log-logarithmic graph with the frequency of occurrence 
of words on the horizontal axis and the frequency of occurrence on the vertical axis.<br/>
用横轴表示按词频顺序排列的词，
竖轴表示词对应的词频，绘制对数图。

![zipf's law](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch04-Morphological-analysis/zipf's_law.png)
