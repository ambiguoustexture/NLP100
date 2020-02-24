# NLP 100 Knocks
言語処理100本ノックは，
実践的な課題に取り組みながら，プログラミング，データ分析，研究のスキルを楽しく習得することを目指した問題集です。<br/>
100 Language Processing Knocks is a collection of problems aimed at learning programming, data analysis, and research skills in a fun way while working on practical tasks. 
This collection is from the Communication Science Laboratory (Inui-Suzuki Lab).<br/>
语言处理一百击是一套旨在 于应对实际任务的过程中 以有趣的方式 学习编程、数据分析和研究技能的习题集。
习题集来自日本东北大学的通讯科学实验室（乾・鈴木研究室）。

素人と初心者。 詳細な説明（コードとファイル）については、各章のフォルダーを参照してください。<br/>
Amateur and novice. For detailed explanations (codes and files), please refer to the folder of each chapter.<br/>
业余新手。详细题解（代码以及文件）请参见每个章节的文件夹。

## 第1章: 準備運動
### 00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

### 01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

### 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

### 03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

### 04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

### 05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

### 06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

### 07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

### 08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
- その他の文字はそのまま出力
- この関数を用い，英語のメッセージを暗号化・復号化せよ．

### 09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

## 第2章: UNIXコマンドの基礎

[hightemp.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt)は，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

### 10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．

### 11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

### 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

### 13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

### 14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

### 15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

### 16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

### 17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

### 18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

### 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

### 20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

### 21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

### 22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

### 23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

### 24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

### 25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．<br/>
Extract the field names and values of the "基礎情報" template included in the article 
and store them as dictionary objects.

### 26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．<br/>
In Step 25, remove MediaWiki's emphasis markup (weak emphasis, emphasis, and strong emphasis) from the template value and convert it to text.

    weak emphasis       ''italics''
    emphasis            '''bold'''
    strong emphasis     '''''both'''''

### 27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．<br/>
In addition to the processing of 26, remove MediaWiki's internal link markup from the template value and convert it to text.

    MediaWiki's internal link markup        [[]]

### 28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．<br/>
In addition to the processing of 27, remove MediaWiki markup from template values as much as possible, and format basic country information.

### 29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）<br/>
Get the URL of the flag image using the contents of the template. (Hint: Call imageinfo of MediaWiki API to convert file references to URLs)

## 第4章: 形態素解析
夏目漱石の小説『吾輩は猫である』の文章（[neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．<br/>
Morphologically analyze the text of Soseki Natsume's novel "I am a cat" using MeCab, 
and save the results in a file called neko.txt.mecab. 
Use this file to implement a program that addresses the following questions.

なお，問題37, 38, 39は[matplotlib](http://matplotlib.org/)
もしくは[Gnuplot](http://www.gnuplot.info/)を用いるとよい．<br>
For problems 37, 38, and 39, use matplotlib or Gnuplot.

### 30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．<br/>
Implement a program that reads the result of morphological analysis (neko.txt.mecab).
However, each morpheme is stored in a mapping type with the surface type (surface), basic type (base), part of speech (pos), and part of speech class 1 (pos1) as keys, and one sentence is represented as a list of morphemes (mapping type) Please.
Use the program you created here for the rest of Chapter 4.

### 31. 動詞
動詞の表層形をすべて抽出せよ．<br/>
Extract all verb surface forms.

### 32. 動詞の原形
動詞の原形をすべて抽出せよ．<br/>
Extract all verb forms.

### 33. サ変名詞
サ変接続の名詞をすべて抽出せよ．<br/>
Extract all nouns which verbs can be formed by adding "する" to.

### 34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．<br/>
Extract a noun phrase where two nouns are connected by "の".

### 35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．<br/>
Extract the concatenation of nouns (nouns that appear consecutively) with the longest match.

### 36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．<br/>
Find the words that appear in the text and their frequency of occurrence, and arrange them in descending order of frequency of appearance.

### 37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．<br/>
Display the 10 most frequently occurring words and their frequency of occurrence in a graph (eg a bar graph).

### 38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．<br/>
Draw a histogram of the frequency of occurrence of the word (the horizontal axis represents the frequency of appearance, and the vertical axis represents the number of types of words whose appearance frequency is represented by a bar graph).
### 39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．<br/>
Plot a log-logarithmic graph with the frequency of occurrence of words on the horizontal axis and the frequency of occurrence on the vertical axis.
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

### 41. 係り受け解析結果の読み込み（文節・係り受け）
Reading dependency analysis results (phrase / dependency) <br/>
读取依存关系分析结果（短语/依存关系）

40に加えて，文節を表すクラス**Chunk**を実装せよ．このクラスは形態素（**Morph**オブジェクト）のリスト（**morphs**），係り先文節インデックス番号（**dst**），係り元文節インデックス番号のリスト（**srcs**）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文を**Chunk**オブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．<br/>
In addition to 40, implement a class Chunk that represents a clause. This class shall have a list of morphemes (Morph objects) (morphs), a target clause index number (dst), and a list of source clause index numbers (srcs) as member variables. Furthermore, read the analysis result of CaboCha of the input text, express one sentence as a list of Chunk objects, and display the character string of the eighth sentence and the destination. Use the program you created here for the rest of Chapter 5. <br/>
在**40**的基础上，实现代表词组的**Chunk**类。
此类拥有一个词素(**40**中的**Morph**对象)列表（**morphs**），一个目标词组索引号（**dst**）和一个依存关系源词组索引号（**srcs**）作为成员变量。
之后，读取输入文本的CaboCha的分析结果，将一个句子表示为**Chunk**对象的列表，并显示第八句的**dst**和**srcs**。
将这里创建的程序用于第5章的其余部分。

### 42. 係り元と係り先の文節の表示
Display of source and destination clauses<br/>
显示源词组和目的词组

係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．<br/>
Extract all the text of the source and destination clauses in tab-delimited format. However, do not output symbols such as punctuation marks.<br/>
以制表符分隔的格式提取源词组和目标词组的所有文本。 但是，请勿输出标点符号等符号。

### 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
Extract clauses containing nouns related to clauses containing verbs<br/>
抽取出包含名词且目的词组包含动词的词组

名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．<br/>
When a phrase containing a noun pertains to a phrase containing a verb, extract them in tab-delimited format. However, do not output symbols such as punctuation marks.<br/>
当包含名词的短语与包含动词的短语相关时，请以制表符分隔的格式提取它们。 但是，请勿输出标点符号等符号。

### 44. 係り受け木の可視化
Visualization of dependency trees
依存句法树的可视化

与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木を[DOT言語](http://ja.wikipedia.org/wiki/DOT言語)に変換し，[Graphviz](http://www.graphviz.org/)を用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，[pydot](https://code.google.com/p/pydot/)を使うとよい．<br/>
Visualize the dependency tree of a given sentence as a directed graph. For visualization, convert the dependency tree to the DOT language and use Graphviz. You can also use pydot to visualize directed graphs directly from Python.<br/>
将给定句子的依存关系树可视化为有向图。 为了可视化，将依赖关系树转换为DOT语言并使用Graphviz。还可以使用pydot直接用Python可视化有向图。

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
