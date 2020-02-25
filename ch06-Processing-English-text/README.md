## 第6章: 英語テキストの処理
Processing English text<br/>
处理英文文本

英語のテキスト（[nlp.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt)）に対して，
以下の処理を実行せよ．<br/>
Perform the following processing on the English text (nlp.txt).<br/>
对英文文本（nlp.txt）执行以下处理。

### 50. 文区切り
Sentence segment<br/>
断句

(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
入力された文書を1行1文の形式で出力せよ．<br/>
(. or ; or : or ? or !) → space → uppercase letters should be regarded as a sentence delimiter, 
and output the input document in the form of one sentence per line.<br/>
(. or ; or : or ? or !) → 空格 → 大写字母应视为句子定界符，并以每行一个句子的形式输出输入文档。
```python
import re

def sentence_segmengt(file):
    with open(file) as text:
        pattren = re.compile(r'''
                            (^.*? [\.|;|:|\?|!])        # (. or ; or : or ? or !)
                            \s                          # space
                            (A-Z).*                     # uppercase letters
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
        for line in text:
            line = line.strip()
            while len(line) > 0:
                match = pattren.match(line)
                if match:
                    yield match.group(1)
                    line = match.group(2)
                else:
                    yield line
                    line = ''

if __name__ == '__main__':
    file = './nlp.txt'
    for sentence in sentence_segmengt(file):
        print(sentence)
```
```zsh
➜ python sentence_segment.py > sentences.txt; head -4 sentences.txt
Natural language processing
From Wikipedia, the free encyclopedia
Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of humani-computer interaction. Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.
History
```

### 51. 単語の切り出し
Word segmentation<br/>
分词

空白を単語の区切りとみなし，
50の出力を入力として受け取り，
1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．<br/>
Treat the space as a word delimiter, 
take 50 outputs as input, 
and output in the form of one word per line. 
However, output a blank line at the end of the sentence.<br/>
将空白视为单词定界符，
以50个输出作为输入，
并以每行一个单词的形式输出。
但是，请在句子末尾输出空白行。
```pytohn
from sentence_segment import sentence_segment

def word_segment(file):
    for sentence in sentence_segment(file):
        for word in sentence.split(' '):
            yield word.rstrip('.,;:?!')
        yield ''

if __name__ == '__main__':
    file = './nlp.txt'
    for word in word_segment(file):
        print(word)
```
```zsh
➜ python word_segment.py > words.txt; head words.txt
Natural
language
processing

From
Wikipedia
the
free
encyclopedia

```
### 52. ステミング
Stemming<br/>
抽取词干

51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，
Porterのステミングアルゴリズムの実装として
[stemming](https://pypi.python.org/pypi/stemming)モジュールを利用するとよい．<br/>
Take the output of 51 as input, 
apply Porter's stemming algorithm, 
and output words and stems in tab-delimited format.
In Python, you can use the [stemming](https://pypi.python.org/pypi/stemming) 
module to implement Porter stemming algorithm.<br/>
将51的输出作为输入，应用Porter词干抽取算法，
并以制表符分隔的格式输出单词和词干.
在Python中，可以使用[stemming](https://pypi.python.org/pypi/stemming)模块来实现Porter词干抽取算法。

```python
from stemming.porter import stem

file = './words.txt'
with open(file) as words:
    for word in words:
        print('%s\t' % word.rstrip(), '%s' % stem(word))
```
```zsh
➜ python word_stemming_by_stemming.py > word_stemming_by_stemming_porter.txt; head word_stemming_by_stemming_porter.txt
Natural	 Natur
language	 languag
processing	 process

From	 From
Wikipedia	 Wikipedia
the	 the
free	 free
encyclopedia	 encyclopedia
```
Porterステミングアルゴリズムの実装として、stemmingモジュールに間違いがあることがわかります。
It can be seen that there are mistakes in the stemming module as implement of Porter stemming algorithm.
可以看出，作为Porter词干算法的实现，stemming模块中存在错误。

### 53. Tokenization
标记化

[Stanford Core NLP](http://nlp.stanford.edu/software/corenlp.shtml)を用い，
入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．<br/>
Use Stanford Core NLP to get the result of parsing the input text in XML format. 
Also read this XML file and output the input text in the form of one word per line.<br/>
使用Stanford Core NLP来获取将输入文本解析为XML格式的结果。 
另外读取此XML文件，并以每行一个单词的形式输出输入的文本。
```python
import os
import subprocess
import xml.etree.ElementTree as ET

file_original = 'nlp.txt'
file_parsed   = 'nlp.txt.xml'


def parse():
    if not os.path.exists(file_parsed):
        subprocess.run(
            'java -cp "/usr/local/lib/stanford-corenlp-full-2018-10-05/*"'
            ' -Xmx3g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + file_original + ' 2>parse.out',
            shell=True,
            check=True)

parse()
root = ET.parse(file_parsed)
for word in root.iter('word'):
    print(word.text)
```
```zsh
➜ python tokenization.py > word_tokenized.txt; head word_tokenized.txt
Natural
language
processing
From
Wikipedia
,
the
free
encyclopedia
Natural
```

### 54. 品詞タグ付け
Part of speech tagging<br/>
词性标注

Stanford Core NLPの解析結果XMLを読み込み，
単語，レンマ，品詞をタブ区切り形式で出力せよ．<br/>
Read the analysis result XML of Stanford Core NLP and output words, 
lemmas and parts of speech in tab-delimited format.<br/>
读取Stanford Core NLP的分析结果XML，
并以制表符分隔的格式输出单词，词条和词性。
```python

```
import xml.etree.ElementTree as ET

file_parsed   = 'nlp.txt.xml'
root = ET.parse(file_parsed)
for token in root.iter('token'):
    print(token.findtext('word'), '\t',\
            token.findtext('lemma'), '\t',\
```zsh
➜ python word_parsed_with_lemma_pos.py > word_parsed_with_lemma_pos.txt; head word_parsed_with_lemma_pos.txt
Natural 	 natural 	 JJ
language 	 language 	 NN
processing 	 processing 	 NN
From 	 from 	 IN
Wikipedia 	 Wikipedia 	 NNP
, 	 , 	 ,
the 	 the 	 DT
free 	 free 	 JJ
encyclopedia 	 encyclopedia 	 NN
Natural 	 natural 	 JJ
```

### 55. 固有表現抽出
入力文中の人名をすべて抜き出せ．

### 56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，
文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
ただし，置換するときは，「代表参照表現（参照表現）」のように，
元の参照表現が分かるように配慮せよ．

### 57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）
を有向グラフとして可視化せよ．
可視化には，係り受け木を[DOT言語](http://ja.wikipedia.org/wiki/DOT言語)に変換し，
[Graphviz](http://www.graphviz.org/)を用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，
[pydot](https://code.google.com/p/pydot/)を使うとよい．

### 58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
ただし，主語，述語，目的語の定義は以下を参考にせよ．

- 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
- 主語: 述語からnsubj関係にある子（dependent）
- 目的語: 述語からdobj関係にある子（dependent）

### 59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．
i入れ子になっている名詞句もすべて表示すること．
