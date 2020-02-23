## 第5章: 係り受け解析
Chapter 5: Dependency Analysis<br/>
第5章：依存句法分析

夏目漱石の小説『吾輩は猫である』の文章（[neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．<br/>
Analysis dependency of the text ([neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)) of Soseki Natsume's novel "I am a cat" using CaboCha, and save the result in a file called neko.txt.cabocha. Use this file to implement a program that addresses the following questions: <br/>
使用 CaboCha 对夏目漱石的小说《我是猫》的文本（[neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)）进行依存句法分析，并将结果保存在名为 neko.txt.cabocha 的文件中。 使用此文件实现解决以下问题的程序：

### 40. 係り受け解析結果の読み込み（形態素）
Reading dependency analysis results (morpheme) <br/>
读取依存关系分析结果（语素）

形態素を表すクラス**Morph**を実装せよ．このクラスは表層形（**surface**），基本形（**base**），品詞（**pos**），品詞細分類1（**pos1**）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文を**Morph**オブジェクトのリストとして表現し，3文目の形態素列を表示せよ．<br/>
Implement the class Morph that represents a morpheme. This class has surface, base, part of speech (pos), and part of speech classification 1 (pos1) as member variables. In addition, read the analysis result of CaboCha (neko.txt.cabocha), store each sentence as a list of Morph objects, and display the morpheme sequence of the third sentence. <br/>
实现代表词素的类Morph。 此类具有**surface**，**base**，**pos**（词性）和**pos1**作为成员变量。
另外，读取 CaboCha（neko.txt.cabocha）的分析结果，将每个句子存储为Morph对象列表，并显示第三个句子的词素列表。

```Python
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
```Shell
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
```Python
import morphology_analysis

class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst    = -1
        self.srcs   = []

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
```Shell
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
```Python
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
```Shell
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
```Python
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
```Shell
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

与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木を[DOT言語](http://ja.wikipedia.org/wiki/DOT言語)に変換し，[Graphviz](http://www.graphviz.org/)を用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，[pydot](https://code.google.com/p/pydot/)を使うとよい．<br/>
Visualize the dependency tree of a given sentence as a directed graph. For visualization, convert the dependency tree to the DOT language and use Graphviz. You can also use pydot to visualize directed graphs directly from Python.<br/>
将给定句子的依存关系树可视化为有向图。 为了可视化，将依赖关系树转换为DOT语言并使用Graphviz。还可以使用pydot直接用Python可视化有向图。
```Python
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
```Shell
➜ python dependency_visualization.py
Please input a sentence --> どこで生れたかとんと見当がつかぬ。
```
![dependency_visualization.png]()

### 45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

- 動詞を含む文節において，最左の動詞の基本形を述語とする
- 述語に係る助詞を格とする
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

    始める  で
    見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

- コーパス中で頻出する述語と格パターンの組み合わせ
- 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）

### 46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

- 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
- 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
    
    始める  で      ここで
    見る    は を   吾輩は ものを

### 47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

- 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
- 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
- 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

    返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

- コーパス中で頻出する述語（サ変接続名詞+を+動詞）
- コーパス中で頻出する述語と助詞パターン

### 48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

- 各文節は（表層形の）形態素列で表現する
- パスの開始文節から終了文節に至るまで，各文節の表現を"**->**"で連結する

「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

    吾輩は -> 見た
    ここで -> 始めて -> 人間という -> ものを -> 見た
    人間という -> ものを -> 見た
    ものを -> 見た

### 49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
- 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
- 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する

また，係り受けパスの形状は，以下の2通りが考えられる．

- 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
- 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示

例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

    Xは | Yで -> 始めて -> 人間という -> ものを | 見た
    Xは | Yという -> ものを | 見た
    Xは | Yを | 見た
    Xで -> 始めて -> Y
    Xで -> 始めて -> 人間という -> Y
    Xという -> Y

