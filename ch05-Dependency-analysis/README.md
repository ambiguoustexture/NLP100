## 第5章: 係り受け解析
Chapter 5: Dependency Analysis<br/>
第5章：依存句法分析

夏目漱石の小説『吾輩は猫である』の文章（[neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．<br/>
Analysis dependency of the text（neko.txt）of Soseki Natsume's novel "I am a cat" using CaboCha, and save the result in a file called neko.txt.cabocha. Use this file to implement a program that addresses the following questions: <br/>
使用 CaboCha 对夏目漱石的小说《我是猫》的文本（neko.txt）进行依存句法分析，并将结果保存在名为 neko.txt.cabocha 的文件中。 使用此文件实现解决以下问题的程序：

### 40. 係り受け解析結果の読み込み（形態素）
Reading dependency analysis results (morpheme) <br/>
读取依存关系分析结果（语素）

形態素を表すクラス**Morph**を実装せよ．このクラスは表層形（**surface**），基本形（**base**），品詞（**pos**），品詞細分類1（**pos1**）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文を**Morph**オブジェクトのリストとして表現し，3文目の形態素列を表示せよ．<br/>
Implement the class Morph that represents a morpheme. This class has surface, base, part of speech (pos), and part of speech classification 1 (pos1) as member variables. In addition, read the analysis result of CaboCha (neko.txt.cabocha), store each sentence as a list of Morph objects, and display the morpheme sequence of the third sentence. <br/>
实现代表词素的类Morph。 此类具有**surface**，**base**，**pos**（词性）和**pos1**作为成员变量。
另外，读取 CaboCha（neko.txt.cabocha）的分析结果，将每个句子存储为Morph对象列表，并显示第三个句子的词素列表。

```python
import CaboCha

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

def morpheme_analysis(file_parsed):
    sentence, sentences = [], []
    with open('neko.txt.cabocha') as text_parsed:
        for line in text_parsed:
            if line[0] == "*" :
                next
            if "\t" in line:
                item = line.strip().split("\t")
                try:
                    surf = item[0]
                    items = item[1].split(",")
                except IndexError:
                    next
                if not item == ['記号,空白,*,*,*,*,\u3000,\u3000,']:
                    sentence.append(Morph(surf, items[6], items[0], items[1]))
            elif "EOS" in line:
                if len(sentence) > 0:
                    sentences.append(sentence)
                sentence = []
    return sentences
```
The morpheme sequence of the third sentence.
```zsh
➜ python morphology_analysis.py
surface:  どこ　　 	base:  どこ　　 	pos:  名詞　　 	pos1:  代名詞
surface:  で　　　 	base:  で　　　 	pos:  助詞　　 	pos1:  格助詞
surface:  生れ　　 	base:  生れる　 	pos:  動詞　　 	pos1:  自立
surface:  た　　　 	base:  た　　　 	pos:  助動詞　 	pos1:  *
surface:  か　　　 	base:  か　　　 	pos:  助詞　　 	pos1:  副助詞／並立助詞／終助詞
surface:  とんと　 	base:  とんと　 	pos:  副詞　　 	pos1:  一般
surface:  見当　　 	base:  見当　　 	pos:  名詞　　 	pos1:  サ変接続
surface:  が　　　 	base:  が　　　 	pos:  助詞　　 	pos1:  格助詞
surface:  つか　　 	base:  つく　　 	pos:  動詞　　 	pos1:  自立
surface:  ぬ　　　 	base:  ぬ　　　 	pos:  助動詞　 	pos1:  *
surface:  。　　　 	base:  。　　　 	pos:  記号　　 	pos1:  句点
```

### 41. 係り受け解析結果の読み込み（文節・係り受け）
Reading dependency analysis results (phrase / dependency) <br/>
读取依存关系分析结果（短语/依存关系）

40に加えて，文節を表すクラス**Chunk**を実装せよ．このクラスは形態素（**Morph**オブジェクト）のリスト（**morphs**），係り先文節インデックス番号（**dst**），係り元文節インデックス番号のリスト（**srcs**）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文を**Chunk**オブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．<br/>
In addition to 40, implement a class Chunk that represents a clause. This class shall have a list of morphemes (Morph objects) (morphs), a target clause index number (dst), and a list of source clause index numbers (srcs) as member variables. Furthermore, read the analysis result of CaboCha of the input text, express one sentence as a list of Chunk objects, and display the character string of the eighth sentence and the destination. Use the program you created here for the rest of Chapter 5. <br/>
在**40**的基础上，实现代表词组的**Chunk**类。
此类拥有一个词素(**40**中的**Morph**对象)列表（**morphs**），一个目标词组索引号（**dst**）和一个依存关系源词组索引号（**srcs**）作为成员变量。
之后，读取输入文本的CaboCha的分析结果，将一个句子表示为**Chunk**对象的列表，并显示第八句的**dst**和**srcs**。
将这里创建的程序用于第5章的其余部分。
```python
import morphology_analysis

class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst    = -1
        self.srcs   = []

    def get_morphs_by_pos(self, pos, pos1=''):
        if len(pos1) > 0:
            return [res for res in self.morphs
                    if (res.pos == pos) and (res.pos1 == pos1)]
        else:
            return [res for res in self.morphs if res.pos == pos]

def chunk_analysis(file_parsed):
    sentences = []
    sentence = []
    for line in file_parsed:
        if line == "EOS\n":
            for index, chunk in enumerate(sentence[:-1]):
                if chunk.dst != -1:
                    sentence[chunk.dst].srcs.append(index)
            sentences.append(sentence)
            sentence = []
        elif line[0] == "*":
            chunk = Chunk()
            chunk.dst = int(line.split()[2].strip("D"))
            sentence.append(chunk)
        else:
            surface = line.split('\t')[0]
            others = line.split('\t')[1].split(",")
            base, pos, pos1 = others[6], others[0], others[1]
            morph = morphology_analysis.Morph(surface, base, pos, pos1)
            sentence[-1].morphs.append(morph)
    return sentences


if __name__ == "__main__":
    file_parsed = './neko.txt.cabocha'
    with open("neko.txt.cabocha", "r") as text_parsed:
        sentences = chunk_analysis(text_parsed)
        # index of the 8th sentence is 10 in fact
        for index, chunk_current in enumerate(sentences[10]):
            chunk_string = ""
            for morph in chunk_current.morphs:
                chunk_string += morph.surface
            print('chunk: ', chunk_string.ljust(8, chr(12288)),\
                    '\tdst: %2d ' % chunk_current.dst,\
                    '\tsrcs: ',chunk_current.srcs)
```
```zsh
➜ python chunk_analysis.py
chunk:  しかし　　　　　 	dst:  9  	srcs:  []
chunk:  その　　　　　　 	dst:  2  	srcs:  []
chunk:  当時は　　　　　 	dst:  5  	srcs:  [1]
chunk:  何という　　　　 	dst:  4  	srcs:  []
chunk:  考も　　　　　　 	dst:  5  	srcs:  [3]
chunk:  なかったから　　 	dst:  9  	srcs:  [2, 4]
chunk:  別段　　　　　　 	dst:  7  	srcs:  []
chunk:  恐し　　　　　　 	dst:  9  	srcs:  [6]
chunk:  いとも　　　　　 	dst:  9  	srcs:  []
chunk:  思わなかった。　 	dst: -1  	srcs:  [0, 5, 7, 8]
```

### 42. 係り元と係り先の文節の表示
Display of source and destination clauses<br/>
显示源词组和目的词组

係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．<br/>
Extract all the text of the source and destination clauses in tab-delimited format. However, do not output symbols such as punctuation marks.<br/>
以制表符分隔的格式提取源词组和目标词组的所有文本。 但是，请勿输出标点符号等符号。
```python
from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'

with open(file_parsed) as text_parsed:
    sentences = chunk_analysis(text_parsed)
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:

                chunk_src = ''
                for morph in chunk.morphs:
                    chunk_src += morph.surface
                chunk_src = chunk_src.strip()
                chunk_dst = ''
                for morph in sentence[chunk.dst].morphs:
                    chunk_dst += morph.surface
                chunk_dst = chunk_dst.strip()
                if '。' in chunk_dst:
                    chunk_dst = chunk_dst[:-1]
                if chunk_dst != '' and chunk_src != '':
                    print('%s\t' % chunk_src, '%s' % chunk_dst)
```
```zsh
➜ python chunk_display.py > chunk_display.txt; head chunk_display.txt
吾輩は	 猫である
名前は	 無い
まだ	 無い
どこで	 生れたか
生れたか	 つかぬ
とんと	 つかぬ
見当が	 つかぬ
何でも	 薄暗い
薄暗い	 所で
じめじめした	 所で
```

### 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
Extract clauses containing nouns related to clauses containing verbs<br/>
抽取出包含名词且目的词组包含动词的词组

名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．<br/>
When a phrase containing a noun pertains to a phrase containing a verb, extract them in tab-delimited format. However, do not output symbols such as punctuation marks.<br/>
当包含名词的短语与包含动词的短语相关时，请以制表符分隔的格式提取它们。 但是，请勿输出标点符号等符号。
```python
from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'

with open(file_parsed) as text_parsed:
    sentences = chunk_analysis(text_parsed)
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:

                flag_nouns = False
                for morph in chunk.morphs:
                    if morph.pos == '名詞':
                        flag_nouns = True
                chunk_nouns = ''
                if flag_nouns:
                    for morph in chunk.morphs:
                        chunk_nouns += morph.surface
                    chunk_nouns = chunk_nouns.strip()
                    if chunk_nouns[-1] == '、':
                        chunk_nouns = chunk_nouns[:-1]

                    flag_verbs = False
                    for morph in sentence[chunk.dst].morphs:
                        if morph.pos == '動詞':
                            flag_verbs = True
                    chunk_verbs = ''
                    if flag_verbs:
                        for morph in sentence[chunk.dst].morphs:
                            chunk_verbs += morph.surface
                        if chunk_verbs[-1] == '。' or chunk_verbs[-1] == '、':
                            chunk_verbs = chunk_verbs[:-1]
                        print('%s\t' % chunk_nouns, '%s' % chunk_verbs)
```
```zsh
➜ python chunk_nouns_related2verbs.py >chunk_nouns_related2verbs.txt; head chunk_nouns_related2verbs.txt
どこで	 生れたか
見当が	 つかぬ
所で	 泣いて
ニャーニャー	 泣いて
いた事だけは	 記憶している
吾輩は	 見た
ここで	 始めて
ものを	 見た
あとで	 聞くと
我々を	 捕えて
```


### 44. 係り受け木の可視化
Visualization of dependency trees
依存句法树的可视化

与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木を[DOT言語](http://ja.wikipedia.org/wiki/DOT言語)に変換し，[Graphviz](http://www.graphviz.org/)を用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，[pydot](https://code.google.com/p/pydot/)を使うとよい．<br/>
Visualize the dependency tree of a given sentence as a directed graph. For visualization, convert the dependency tree to the DOT language and use Graphviz. You can also use pydot to visualize directed graphs directly from Python.<br/>
将给定句子的依存关系树可视化为有向图。 为了可视化，将依赖关系树转换为DOT语言并使用Graphviz。还可以使用pydot直接用Python可视化有向图。
```python
from chunk_analysis import chunk_analysis
import CaboCha
import pydotplus as pydot

file_parsed = './sentence_input.txt.cabocha'
with open(file_parsed, mode='w') as sentence_parsed:
    cabocha = CaboCha.Parser()
    sentence_parsed.write(cabocha.parse(input('Please input a sentence --> ')).\
            toString(CaboCha.FORMAT_LATTICE))

with open(file_parsed) as text_parsed:
    sentences = chunk_analysis(text_parsed)
    for sentence in sentences:
        edges = []
        for index, chunk in enumerate(sentence):
            if chunk.dst != -1:
                chunk_src = ''
                for morph in chunk.morphs:
                    chunk_src += morph.surface
                chunk_src = chunk_src.strip()
                chunk_dst = ''
                for morph in sentence[chunk.dst].morphs:
                    chunk_dst += morph.surface
                chunk_dst = chunk_dst.strip()
                if '。' in chunk_dst:
                    chunk_dst = chunk_dst[:-1]
                if chunk_src != '' and chunk_dst != '':
                    edges.append(((index, chunk_src), (chunk.dst, chunk_dst)))

        if len(edges) > 0:
            tree = pydot.graph_from_edges(edges, directed=True)
            tree.write_png('./dependency_visualization.png')
```
```zsh
➜ python dependency_visualization.py
Please input a sentence --> どこで生れたかとんと見当がつかぬ。
```
![dependencyVisualization.png](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch05-Dependency-analysis/dependency_visualization.png)

### 45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．<br/>
Consider the sentences used this time as a corpus and want to investigate the possible cases of Japanese predicates. 
Think of a verb as a predicate and a particle in a clause related to the verb as a case, 
and output the predicate and the case in tab-separated format. 
However, the output should satisfy the following specifications.<br/>
将这次使用的句子视为语料库，并希望调查日语谓语的可能情况。 将动词视为谓词，并将与该动词相关的从句中的质点作为格，并以制表符分隔的格式输出谓词和格。 但是，输出应满足以下规格。

- 動詞を含む文節において，最左の動詞の基本形を述語とする<br/>
In a clause containing a verb, use the basic form of the leftmost verb as a predicate<br/>
在包含动词的子句中，使用最左边动词的基本形式作为谓词

- 述語に係る助詞を格とする<br/>
The case of a particle associated with a predicate<br/>
谓词的情况

- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる<br/>
When there are multiple particles (clauses) related to a predicate, all particles are arranged in dictionary order with space delimiters<br/>
当有多个与谓词相关的助词（子句）时，所有助词均按字典顺序排列，并带有空格分隔符

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．<br/>
Consider the example sentence (the eighth sentence of neko.txt.cabocha), "吾輩はここで始めて人間というものを見た". This sentence contains two verbs, "始める" and "見る", and the phrase for "始める" is analyzed as "ここで", and the phrase for "見る" is analyzed as "吾輩は" and "ものを". Should produce the following output:<br/>
考虑例句（neko.txt.cabocha的第八句），“吾輩はここで始めて人間というものを見た”。 该句子包含两个动词“始める”和“見る”，“始める”的词组中助词被分析为“ここで”，而“見る”的短语中被分析为“吾輩は”和“ものを”。 应按以下输出：

    始める  で
    見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．<br/>
Save the output of this program to a file and check the following using UNIX commands.<br>
将该程序的输出保存到文件中，然后使用UNIX命令检查以下内容。

- コーパス中で頻出する述語と格パターンの組み合わせ<br/>
Combinations of predicates and case patterns that occur frequently in the corpus<br/>
语料库中频繁出现的谓词和案例模式的组合

- 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）<br/>
Case patterns of verbs "する", "見る" and "与える" 
(arrange in descending order of appearance frequency in the corpus)<br/>
动词“する”，“見る”和“与える”的格模式（在语料库中以频率降序排列）
```python
from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './verbs_case_result.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)

    for sentence in sentences:
        for chunk in sentence:
            verbs = chunk.get_morphs_by_pos('動詞')
            if len(verbs) < 1:
                continue
            particles = []
            for src in chunk.srcs:
                particles_in_chunk = sentence[src].get_morphs_by_pos('助詞')
                if len(particles_in_chunk) > 1:
                    case_particles = sentence[src].get_morphs_by_pos('助詞', '格助詞')
                    if len(case_particles) > 0:
                        particles_in_chunk = case_particles
                if len(particles_in_chunk) > 0:
                    particles.append(particles_in_chunk[-1])
            if len(particles) < 1:
                continue
            text_result.write('{}\t{}\n'\
                    .format(verbs[0].base, ' '.join(sorted(particle.surface for particle in particles))))
```
```zsh
➜ python verbs_case.py; head verbs_case_result.txt
生れる	で
つく	か が
泣く	で
する	て は
始める	で
見る	は を
聞く	で
捕える	を
煮る	て
食う	て
```
UNIXコマンドを用いて確認<br/>
Check using UNIX commands<br/>
使用UNIX命令检查
```zsh
➜ sort verbs_case_result.txt | uniq -c | sort -n -r > verbs_case_result_uniqed.txt; head verbs_case_result_uniqed.txt
 723 云う	と
 453 する	を
 342 思う	と
 217 なる	に
 203 する	に
 202 ある	が
 175 見る	て
 164 する	と
 118 する	に を
 117 する	が
➜ grep "^する\s" verbs_case_result.txt | sort | uniq -c | sort -n -r > verbs_case_result_uniqed_suru.txt; head verbs_case_result_uniqed_suru.txt
 453 する	を
 203 する	に
 164 する	と
 118 する	に を
 117 する	が
  90 する	て を
  73 する	は
  61 する	て
  60 する	が を
  54 する	と を
➜ grep "^見る\s" verbs_case_result.txt | sort | uniq -c | sort -n -r > verbs_case_result_uniqed_miru.txt; head verbs_case_result_uniqed_miru.txt
 175 見る	て
  98 見る	を
  23 見る	て て
  20 見る	から
  18 見る	と
  15 見る	て を
  13 見る	で
  12 見る	から て
  11 見る	て は
   9 見る	に
➜ grep "^与える\s" verbs_case_result.txt | sort | uniq -c | sort -n -r > verbs_case_result_uniqed_ataeru.txt; head verbs_case_result_uniqed_ataeru.txt
   4 与える	に を
   2 与える	て に は を
   2 与える	て に を
   1 与える	けれども に を
   1 与える	として を
   1 与える	に に対して も
   1 与える	が て と に は は を
   1 与える	て に に は を
   1 与える	て と は を
   1 与える	で に を
```

### 46. 動詞の格フレーム情報の抽出
Extraction of verb case frame information<br/>
抽取动词格框架信息

45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．<br/>
Modify the 45 program and output the term (the clause itself related to the predicate) in tab-delimited format following the predicate and case pattern. Satisfy the following specifications in addition to the 45 specifications.
修改45的程序，并在谓词和格模式之后以制表符分隔的格式输出述语（与谓词相关的子句本身）。 
除了45的格式外，还满足以下规格。

- 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）<br/>
The term is the word sequence of the phrase related to the predicate (the trailing particle need not be removed)<br/>
该项是与谓词相关的短语的词序（不需要删除其后的助词）
- 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる<br/>
If there are multiple clauses related to the predicate, arrange them in the same criteria and order as the particles, separated by spaces.<br/>
如果存在与谓词相关的多个助词，请按照与该助词相同的条件和顺序排列它们，并用空格分隔。

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．<br/>
Consider the example sentence (the eighth sentence of neko.txt.cabocha), "吾輩はここで始めて人間というものを見た".
This sentence contains two verbs, "始める" and "見る", and the phrase for "始める" is analyzed as "here", and the phrase for "見る" is analyzed as "吾輩は" and "ものを". Should produce the following output:<br/>
考虑例句（neko.txt.cabocha的第八句），“吾輩はここで始めて人間というものを見た”。 该句子包含两个动词“始める”和“見る”，“始める”的短语被分析为“ここで”，而“見る”的短语被分析为“吾輩は”和“ものを”。 应产生以下输出：

    
    始める  で      ここで
    見る    は を   吾輩は ものを

```python
from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './verbs_case_frame.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)

    for sentence in sentences:
        for chunk in sentence:
            verbs = chunk.get_morphs_by_pos('動詞')

            if len(verbs) < 1:
                continue

            chunks_with_particle = []

            for src in chunk.srcs:
                if len(sentence[src].get_case_particle()) > 0:
                    chunks_with_particle.append(sentence[src])

            if len(chunks_with_particle) < 1:
                continue

            chunks_with_particle.sort(key = lambda chunk: chunk.get_case_particle())

            text_result.write('{}\t{}\t{}\n'.\
                    format(\
                    verbs[0].base,\
                    ' '.join(chunk.get_case_particle() for chunk in chunks_with_particle),\
                    ' '.join(chunk.get_chunk_string()  for chunk in chunks_with_particle)
                        ))
```
```zsh
➜ python verbs_case_frame.py > verbs_case_frame.txt;head verbs_case_frame.txt
生れる	で	どこで
つく	か が	生れたか 見当が
泣く	で	所で
する	て は	泣いて いた事だけは
始める	で	ここで
見る	は を	吾輩は ものを
聞く	で	あとで
捕える	を	我々を
煮る	て	捕えて
食う	て	煮て
```

### 47. 機能動詞構文のマイニング
Mining functional verb constructions<br/>
挖掘功能动词结构

動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．
Focus only on the case where the verb contains the "サ変接続名詞".
Modify the 46 programs to satisfy the following specifications.
仅关注动词包含"サ変接続名詞"的情况。 修改46的程序以满足以下规格。

- 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする<br/>
Only when the phrase composed of "サ変接続名詞+を（助詞）" relates to a verb<br/>
仅当由“サ変接続名詞+を（助詞）”组成的短语与动词相关时

- 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる<br/>
The predicate shall be "sa-modifying noun + + the basic form of the verb", and if there are multiple verbs in the phrase, use the leftmost verb<vr/>
谓词应为“サ変接続名詞+を+動詞の基本形”，当短语中有多个动词时，使用最左边的动词。

- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
When there are multiple particles (clauses) related to a predicate, 
all particles are arranged in dictionary order with space delimiters<br/>
当有多个与谓词相关的助词（子句）时，所有助词均按字典顺序排列，并带有空格分隔

- 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
If there are multiple clauses related to the predicate, list all terms separated by spaces (align with the order of particles)<br/>
如果存在与该谓词相关的多个子句，列出所有用空格分隔的谓词（与该助词的顺序对齐）


例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．<br/>
For example, the sentence "別段くるにも及ばんさと、主人は手紙に返事をする。" should produce the following output:<br/>
例如，句子“別段くるにも及ばんさと、主人は手紙に返事をする。”应该产生以下输出：

    返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．<br/>
Save the output of the program to a file and check the following using UNIX commands.<br/>
将该程序的输出保存到文件中，然后使用UNIX命令检查以下内容。

- コーパス中で頻出する述語（サ変接続名詞+を+動詞）<br/>
Frequent predicates in the corpus (サ変接続名詞+を+動詞)<br/>
语料库中的惯用谓词（サ変接続名詞+を+動詞）

- コーパス中で頻出する述語と助詞パターン<br/>
Frequent predicates and particle patterns in the corpus<br/>
语料库中的惯用谓词和助词模式
```python
file_parsed = './neko.txt.cabocha'
file_result = './verbs_functional_constructions.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)

    for sentence in sentences:
        for chunk in sentence:
            verbs = chunk.get_morphs_by_pos('動詞')

            if len(verbs) < 1:
                continue

            chunks_with_particle = []
            for src in chunk.srcs:
                if len(sentence[src].get_case_particle()) > 0:
                    chunks_with_particle.append(sentence[src])
            if len(chunks_with_particle) < 1:
                continue

            sahen_wo_particle = ''
            for chunk_src in chunks_with_particle:
                sahen_wo_particle = chunk_src.get_sahen_wo_particle()
                if len(sahen_wo_particle) > 0:
                    chunk_need_remove = chunk_src
                    break
            if len(sahen_wo_particle) < 1:
                continue

            chunks_with_particle.remove(chunk_need_remove)
            chunks_with_particle.sort(key = lambda chunk: chunk.get_case_particle())

            text_result.write('{}\t{}\t{}\n'.\
                    format(\
                    sahen_wo_particle + verbs[0].base,\
                    ' '.join([chunk.get_case_particle() for chunk in chunks_with_particle]),\
                    ' '.join([chunk.get_chunk_string()  for chunk in chunks_with_particle])
                        ))
```
```zsh
➜ python verbs_functional_constructions.py > verbs_functional_constructions.txt; head verbs_functional_constructions.txt
決心をする	と	こうと
返報をする	んで	偸んで
昼寝をする
昼寝をする	が	彼が
迫害を加える	て	追い廻して
生活をする	が を	我等猫族が 愛を
話をする
投書をする	て へ	やって ほととぎすへ
話をする	に	時に
写生をする
```
UNIXコマンドを用いて確認<br/>
Check using UNIX commands<br/>
使用UNIX命令检查
```zsh
➜ cut -f1 verbs_functional_constructions.txt | sort | uniq -c | sort -n -r > verbs_functional_constructions_predicate.txt; head verbs_functional_constructions_predicate.txt
  30 返事をする
  21 挨拶をする
  16 話をする
  14 真似をする
  13 喧嘩をする
   8 質問をする
   7 運動をする
   6 注意をする
   6 昼寝をする
   6 話を聞く
➜ cut -f1,2 verbs_functional_constructions.txt | sort | uniq -c | sort -n -r > verbs_functional_constructions_predicate_particle.txt; head verbs_functional_constructions_predicate_particle.txt
   8 真似をする
   6 返事をする	と
   6 運動をする
   6 喧嘩をする
   4 挨拶をする	から
   4 返事をする	と は
   4 挨拶をする	と
   4 返事をする
   4 話を聞く
   4 話をする
```

### 48. 名詞から根へのパスの抽出
Extraction of path from noun to root<br/>
从名词到依存树根的路径提取

文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ.
ただし，構文木上のパスは以下の仕様を満たすものとする．<br/>
For a phrase containing all nouns in the sentence, 
extract the path from that phrase to the root of the parse tree. 
However, the path on the syntax tree shall satisfy the following specifications.<br/>
对于包含句子中所有名词的短语，提取从该短语到依存树的根的路径。 但是，依存句法树上的路径应满足以下规范。

- 各文節は（表層形の）形態素列で表現する<br/>
Each clause is represented by a morpheme sequence (surface type)<br/>
每个短语由一个语素序列（surface类型）表示

- パスの開始文節から終了文節に至るまで，各文節の表現を"**->**"で連結する<br/>
From the start clause of the path to the end clause, connect the expressions of each clause with "**->**"<br/>
从路径的开始短语到结束短语，将每个短语的表达式用“**->**”连接

「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．<br/>
From the sentence "吾輩はここで始めて人間というものを見た" (the eighth sentence in neko.txt.cabocha), 
you should get the following output:<br/>
对于句子“吾輩はここで始めて人間というものを見た”（neko.txt.cabocha中的第八句话），应该获得以下输出：
    吾輩は -> 見た
    ここで -> 始めて -> 人間という -> ものを -> 見た
    人間という -> ものを -> 見た
    ものを -> 見た

```python
from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './nouns2root.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)

    for sentence in sentences:
        for chunk in sentence:
            if len(chunk.get_morphs_by_pos('名詞')) > 0:
                if chunk.get_chunk_string() != '':
                    text_result.write(chunk.get_chunk_string())

                dst = chunk.dst
                while dst != -1:
                    text_result.write(' -> ' + sentence[dst].get_chunk_string())
                    dst = sentence[dst].dst
                text_result.write('\n')
```
```zsh
➜ python nouns2root.py > nouns2root.txt; head nouns2root.txt
一
吾輩は -> 猫である
猫である
名前は -> 無い
どこで -> 生れたか -> つかぬ
見当が -> つかぬ
何でも -> 薄暗い -> 所で -> 泣いて -> 記憶している
所で -> 泣いて -> 記憶している
ニャーニャー -> 泣いて -> 記憶している
いた事だけは -> 記憶している
```

### 49. 名詞間の係り受けパスの抽出
Extraction of dependency paths between nouns<br/>
提取名词之间的依赖路径

文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiとj*（i<j）*のとき，係り受けパスは以下の仕様を満たすものとする．<br/>
Extract the shortest dependency path that connects all pairs of noun phrases in the sentence. However, when the phrase numbers of the noun phrase pair are i and j *(i<j)*, the dependency path shall satisfy the following specifications.<br/>
提取连接句子中所有成对名词短语的最短依赖路径。 
但是，当名词短语对的短语编号为i和j*（i<j）*时，从属路径应满足以下规范。

- 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する<br/>
As in Question 48, the path is expressed by connecting the expressions of each clause from the start clause to the end clause (surface layer morpheme sequence) with "->"<br/>
如问题48所示，通过用“->”连接从开始子句到结束子句的每个子句的表达式（surface的morph序列）来表示路径。

- 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する<br/>
Replace noun phrases in clauses i and j with X and Y, respectively<br/>
分别用X和Y替换短语i和j中的名词短语

また，係り受けパスの形状は，以下の2通りが考えられる．<br/>
The shape of the dependency path can be the following two types.<br/>
依存路径的形状可以是以下两种类型。

- 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示<br/>
If clause j exists on the path from clause i to the root of the syntax tree: 
display the path from clause i to clause j<br/>
如果短语i到依存语法树根的路径上存在短语j：显示从短语i到短语j的路径

- 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示<br/>
Other than the above, when a common clause k intersects on the path from clause i to clause j to the root of the syntax tree: the path from clause i to clause k and the path from clause j to clause k, clause k Display the contents of "" concatenated with "|"<br/>
除上述之外，当公共短语k在从短语i到短语j到语法树的根的路径上相交时：
短语i到短语k之前的路径，短语j到短语k之前的路径以及短语k的内容用“ |”连接

例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．<br/>
For example, from the sentence "吾輩はここで始めて人間というものを見た。" (the eighth sentence in neko.txt.cabocha), 
the following output should be obtained.<br/>
例如，句子“吾輩はここで始めて人間というものを見た。”（neko.txt.cabocha中的第八个句子）应产生以下输出。

    Xは | Yで -> 始めて -> 人間という -> ものを | 見た
    Xは | Yという -> ものを | 見た
    Xは | Yを | 見た
    Xで -> 始めて -> Y
    Xで -> 始めて -> 人間という -> Y
    Xという -> Y

```python
from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './nouns_dependency.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)
    for sentence in sentences:
        index_nouns = [index for index in range(len(sentence))
                if len(sentence[index].get_morphs_by_pos('名詞')) > 0]
        if len(index_nouns) < 2:
            continue
        for index, index_x in enumerate(index_nouns[:-1]):
            for index_y in index_nouns[index + 1:]:
                flag_intersect  = False
                index_intersect = -1
                path = set()

                dst = sentence[index_x].dst
                while dst != -1:
                    if dst == index_y:
                        flag_intersect = True
                        break
                    path.add(dst)
                    dst = sentence[dst].dst

                if not flag_intersect:
                    dst = sentence[index_y].dst
                    while dst != -1:
                        if dst in path:
                            index_intersect = dst
                            break
                        else :
                            dst = sentence[dst].dst
                if index_intersect == -1:
                    text_result.write(sentence[index_x].get_original_surface('X'))
                    dst = sentence[index_x].dst
                    while dst != -1:
                        if dst == index_y:
                            text_result.write(' -> ' + sentence[dst].get_original_surface('Y', True))
                            break
                        else :
                            text_result.write(' -> ' + sentence[dst].get_chunk_string())
                        dst = sentence[dst].dst
                    text_result.write('\n')
                else :
                    text_result.write(sentence[index].get_original_surface('X'))
                    dst = sentence[index_x].dst
                    while dst != index_intersect:
                        text_result.write(' -> ' + sentence[dst].get_chunk_string())
                        dst = sentence[dst].dst

                    text_result.write(' | ')

                    text_result.write(sentence[index_y].get_original_surface('Y'))
                    dst = sentence[index_y].dst
                    while dst != index_intersect:
                        text_result.write(' -> ' + sentence[dst].get_chunk_string())
                        dst = sentence[dst].dst
                    text_result.write(' | ')

                    text_result.write(sentence[index_intersect].get_chunk_string())
                    text_result.write('\n')
```
```zsh
➜ python nouns_dependency.py; head nouns_dependency.txt
Xは -> Y
Xで -> 生れたか | Yが | つかぬ
Xでも -> 薄暗い -> Y
Xでも -> 薄暗い -> 所で | Y | 泣いて
Xでも -> 薄暗い -> 所で -> 泣いて | Yだけは | 記憶している
Xでも -> 薄暗い -> 所で -> 泣いて -> Y
薄暗い | Y | 泣いて
薄暗い -> 泣いて | Yだけは | 記憶している
Xで -> 泣いて -> Y
じめじめした -> 泣いて | Yだけは | 記憶している
```
