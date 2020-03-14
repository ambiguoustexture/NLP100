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
Preparation exercise<br/>
准备练习

### 00. 文字列の逆順
Reverse string
逆置字符串

文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．<br/>
Obtain a string in which the characters in the string "stressed" are reversed 
(from the end to the beginning).<br/>
从字符串"stressed"获得一个反转（从结尾到开头）的字符串。

### 01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．<br/>
Take the 1st, 3rd, 5th, and 7th characters of the character string "パタトクカシーー" 
and obtain a concatenated character string.<br/>
取字符串“パタトクカシーー”的第1，第3，第5和第7个字符，以获得串联的字符串。

### 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．<br/>
Obtain the character string "パタトクカシーー" 
by connecting the letters "パトカー" + "タクシー" alternately from the beginning.<br/>
通过从头开始交替连接“パトカー” +“タクシー”的字符来获取字符串“パタトクカシーー”。

### 03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．<br/>
Break the sentence 
"Now I need a drink, alcoholic course, after the heavy lectures involving quantum mechanics." 
into words, and make a list of the number of characters (in the alphabet) 
of each word in order of appearance.<br/>
把句子“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
分解为单词，
并创建一个列表，其中是按从头开始出现的顺序排列的每个单词的字符数。

### 04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）
への連想配列（辞書型もしくはマップ型）を作成せよ．<br/>
Break the sentence 
"Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. Arthur King Can." 
into words.
Extract the first character of word 1, 5, 6, 7, 8, 9, 15, 16, 19, 
the first two characters of other words.
And creat an associative array (dictionary or map type) of 
the extracted string and the word position (the number of the word from the beginning).<br/>
获得句子“Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
的第1、5、6、7、8、9、15、16、19 个单词的第一个字符，其他单词的前两个字符，
另外，对提取到的字符串和单词的位置（从头开始的单词次序）创建关联数组（字典或map类型）。

### 05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．<br/>
Create a function to get n-gram from a given sequence (string, list, etc.). 
Using this function, get the word bi-gram and character bi-gram 
from the sentence "I am an NLPer".<br/>
创建一个函数，对给定的序列（字符串，列表等）得到n-gram。
使用此函数，从句子“I am a NLPer”中获取词bi-gram和字符bi-gram。

### 06. 集合
Set

"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．<br/>
Find the set of character bi-grams 
included in "paraparaparadise" and "paragraph" as X and Y, 
respectively, find the union, intersection, and difference of X and Y. 
In addition, check if the bi-gram 'se' is included in X and Y.<br/>
分别找到包含在“paraparaparadise”和“paragraph”中的字符bi-gram集合，作为X和Y，
并找到X和Y的并集，交集和差。
另外，检查X和Y中是否包含“se”的bi-gram。

### 07. テンプレートによる文生成
Sentence generation by template<br/>
通过模板生成句子

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．<br/>
Implement a function that accepts the arguments x, y, z 
and returns the string "x時のyはz". 
Check the execution result with x=12, y="気温", z=22.4.<br/>
实现一个接受参数x，y，z并返回字符串“x時のyはz”的函数。
用x=12, y="気温", z=22.4测试结果。

### 08. 暗号文
Cryptogram<br/>
密文

与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．<br/>
Implement the cipher function that converts each character 
of the given string according to the following specifications.<br/>
实现加密功能，该功能将根据以下规范转换给定字符串的每个字符。

英小文字ならば(219 - 文字コード)の文字に置換<br/>
If lowercase, replace with (219-character code)<br/>
替换小写字母（219 - ASCII）

- その他の文字はそのまま出力<br/>
Other characters are output as it is<br/>
其他字符按原样输出

- この関数を用い，英語のメッセージを暗号化・復号化せよ．<br/>
Use this function to encrypt and decrypt English messages.<br/>
使用此功能可以加密和解密英文消息。

### 09. Typoglycemia
スペースで区切られた単語列に対して，
各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば
"I couldn't believe that I could actually understand what I was reading : 
the phenomenal power of the human mind ."
）を与え，
その実行結果を確認せよ．<br/>
For a word sequence separated by spaces, 
write a program that leaves the characters at the beginning and end of each word 
and rearranges the order of the other characters randomly. 
However, words with a length of 4 or less are not sorted. 
Give an appropriate English sentence (eg, 
"I couldn't believe that I could actually understand what I was reading: 
the phenomenal power of the human mind."
) And check the results.<br/>
对于由空格分隔的单词序列，创建一个程序，
该程序保留每个单词开头和结尾的字符，
并随机重新排列其他字符的顺序。 
但是，长度不超过4的单词不会被重排。
应用于一个适当的英语句子（例如，
“I couldn't believe that I could actually understand what I was reading : 
the phenomenal power of the human mind .”
）然后检查结果。

## 第2章: UNIXコマンドの基礎
[hightemp.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt)は，
日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．<br/>
[hightemp.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt) 
is a file that stores the record of the highest temperature in Japan 
in the tab-delimited format of "prefecture", "point", "℃", and "day". 
Create a program that performs the following processing and execute hightemp.txt as an input file. 
In addition, execute the same process using UNIX commands 
and check the execution result of the program.<br/>
[hightemp.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt)
是一份以制表符分隔的格式存储“日本最高温度”的文件，
格式为“县”，“地点”，“°C”和“日期”。
创建可执行以下处理的程序，并以hightemp.txt为输入文件。 
另外，使用UNIX命令执行相同的处理并检查程序的执行结果。

### 10. 行数のカウント
Row count<br/>
计算行数

行数をカウントせよ．確認には*wc*コマンドを用いよ．<br/>
Count the number of lines. Use *wc* command for confirmation.
计算行数。 使用*wc*命令进行确认。

### 11. タブをスペースに置換
Replace tabs with spaces<br/>
用空格替换制表符

タブ1文字につきスペース1文字に置換せよ．
確認には*sed*コマンド，*tr*コマンド，もしくは*expand*コマンドを用いよ．
Replace each tab with one space. 
Use the *sed* command, *tr* command, or *expand* command for confirmation.<br/>
将每个制表符替换为一个空格。 使用sed，tr 或 expand命令进行确认。

### 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
Save the first column in col1.txt and the second column in col2.txt<br/>
将第一列保存在col1.txt中，将第二列保存在col2.txt中

各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認には*cut*コマンドを用いよ．<br/>
Save only the first column of each row to col1.txt and save the second column to col2.txt. 
Use the *cut* command for confirmation.<br/>
仅将每行的第一列保存到col1.txt，将第二列保存到col2.txt。 
使用*cut*命令进行确认。

### 13. col1.txtとcol2.txtをマージ
merge col1.txt and col2.txt<br/>
合并col1.txt和col2.txt

12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認には*paste*コマンドを用いよ．<br/>
Combine col1.txt and col2.txt created in step 12, 
and create a text file in which the first and second columns of the original file are tab-separated. 
Use the *paste* command for confirmation.<br/>
合并在步骤12中创建的col1.txt和col2.txt为一个文本文件，
其中原始文件的第一和第二列用制表符分隔。使用*paste*命令进行确认。

### 14. 先頭からN行を出力
Output first N lines<br/>
输出前N行

自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認には*head*コマンドを用いよ．<br/>
Receive the natural number N by means of a command line argument or other means 
and display only the first N lines of the input. 
Use the *head* command for confirmation.<br/>
通过命令行参数或其他方式获取自然数N，
只显示输入的前N行。 
使用*head*命令进行确认。

### 15. 末尾のN行を出力
Output last N lines<br/>
输出后N行

自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．
確認には*tail*コマンドを用いよ．<br/>
Receive the natural number N by means of command line arguments or other means 
and display only the last N lines of the input. 
Use the *tail* command for confirmation.<br/>
通过命令行参数或其他方式获取自然数N，
只显示输入文件的后N行。 
使用*tail*命令进行确认。

### 16. ファイルをN分割する
Divide files into N parts<br/>
将文件分成N个

自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．
同様の処理を*split*コマンドで実現せよ．<br/>
Receive the natural number N by means of command line arguments 
and divide the input file into N lines. 
Perform the same processing with the *split* command.<br/>
通过命令行参数获取自然数N并将输入文件分为N行。
使用*split*命令执行相同的处理。

### 17. １列目の文字列の異なり
Difference of the string in column<br/>
第一个字符串的差异

1列目の文字列の種類（異なる文字列の集合）を求めよ．確認には*sort*, *uniq*コマンドを用いよ．
Find the type of string in the first column (a set of different strings). 
Use the *sort* and *uniq* commands for confirmation.<br/>
找到第一列中字符串的（一个不同字符串的集合）种类。
使用*sort*和*uniq*命令进行确认。

### 18. 各行を3コラム目の数値の降順にソート
Sort each row in descending order of the numerical value in the third column<br/>
按第三列中数值的降序对每一行进行排序

各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認には*sort*コマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）.<br/>
Sort each line in the reverse order of the numerical values in the third column. 
(Note: Sort without changing the contents of each line.) 
Use the *sort* command for confirmation 
(this problem does not have to match the result of running the command).<br/>
按第三列中数值的相反顺序对每行进行排序（注意：在不更改每行内容的情况下进行排序）。 
使用*sort*命令进行确认（此问题不必与运行命令行的结果相匹配）。

### 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
Obtain the frequency of appearance of the character string 
in the first column of each line, 
and arrange them in descending order of frequency<br/>
获取每行第一列中字符串出现的频率，并按频率降序排列

各行の1列目の文字列の出現頻度を求め，
その高い順に並べて表示せよ．
確認には*cut*, *uniq*, *sort*コマンドを用いよ．<br/>
<br/>
Find the appearance frequency of the character string in the first column of each line, 
and display them in descending order. Use the *cut*, *uniq*, and *sort* commands for confirmation.<br/>
查找每行中第一列中字符串的出现频率，
并以降序显示。
使用*cut*，*uniq*和*sort*命令进行确认。

# 第3章: 正規表現
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


### 53. Tokenization
标记化

[Stanford Core NLP](http://nlp.stanford.edu/software/corenlp.shtml)を用い，
入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．<br/>
Use Stanford Core NLP to get the result of parsing the input text in XML format.
Also read this XML file and output the input text in the form of one word per line.<br/>
使用Stanford Core NLP来获取将输入文本解析为XML格式的结果。
另外读取此XML文件，并以每行一个单词的形式输出输入的文本。

### 54. 品詞タグ付け
Part of speech tagging<br/>
词性标注

Stanford Core NLPの解析結果XMLを読み込み，
単語，レンマ，品詞をタブ区切り形式で出力せよ．<br/>
Read the analysis result XML of Stanford Core NLP and output words,
lemmas and parts of speech in tab-delimited format.<br/>
读取Stanford Core NLP的分析结果XML，
并以制表符分隔的格式输出单词，词条和词性。

### 55. 固有表現抽出
Named entity extraction<br/>
命名实体提取

入力文中の人名をすべて抜き出せ．<br/>
Extract all the person names in the input sentence.
提取输入句子中的所有人员姓名。

### 56. 共参照解析
Coreference analysis<br/>
共指消解

Stanford Core NLPの共参照解析の結果に基づき，
文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
ただし，置換するときは，「代表参照表現（参照表現）」のように，
元の参照表現が分かるように配慮せよ．<br/>
Based on the results of the Stanford Core NLP co-reference analysis,
replace the reference in the text with a representative mention.<br/>
根据Stanford Core NLP共指消解的结果，
用具有代表性的指代（代表性指代）替换句子中的参考表达（指代）。

### 57. 係り受け解析
Dependency analysis<br/>
依存分析

Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）
を有向グラフとして可視化せよ．
可視化には，係り受け木を[DOT言語](http://ja.wikipedia.org/wiki/DOT言語)に変換し，
[Graphviz](http://www.graphviz.org/)を用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，
[pydot](https://code.google.com/p/pydot/)を使うとよい．
Visualize the results of Stanford Core NLP's dependency analysis
(collapsed-dependencies) as a directed graph.
For visualization, convert the dependency tree to the DOT language and use Graphviz.
You can also use pydot to visualize directed graphs directly from Python.<br/>
将Stanford Core NLP的依存分析（折叠依存关系）结果可视化为有向图。
为了可视化，将依赖关系树转换为DOT语言并使用Graphviz。也可以使用pydot直接从Python可视化有向图。

### 58. タプルの抽出
Extract tuples<br/>
提取元组

Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
ただし，主語，述語，目的語の定義は以下を参考にせよ．<br/>
Based on the results of the Stanford Core NLP dependency analysis (collapsed-dependencies),
output a set of "subject, predicate, object" in tab-delimited format.
Please refer to the following for the definition of the subject, predicate, and object.<br/>
根据Stanford Core NLP依赖性分析（折叠依赖性）的结果，
以制表符分隔的格式输出一组“主语，谓语，宾语”。
请参阅以下有关主语，谓语和宾语的定义。

- 述語: nsubj関係とdobj関係の子（dependant）を持つ単語<br/>
Predicate: words with children (dependant) of nsubj relation and dobj relation
谓语：带有nsubj关系和dobj关系的子项（从属）的单词

- 主語: 述語からnsubj関係にある子（dependent）<br/>
Subject: child with nsubj relationship from predicate (dependent)<br/>
主语：与谓语具有nsubj关系的孩子（从属）

- 目的語: 述語からdobj関係にある子（dependent）<br/>
Object: child in dobj relationship from predicate (dependent)
宾语：谓语中的dobj关系中的子对象（从属）

### 59. S式の解析
Analysis of S-expression<br/>
S表达分析

Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．
i入れ子になっている名詞句もすべて表示すること．
Read the result (S expression) of the phrase structure analysis of Stanford Core NLP
and display all noun phrases (NP) in the sentence.
Display all nested noun phrases.<br/>
读取Stanford Core NLP短语结构分析的结果（S表达式），
并在句子中显示所有名词短语（NP）。
显示所有嵌套的名词短语。

## 第7章: データベース
Database<br/>
数据库

[artist.json.gz](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz)は，
オープンな音楽データベース[MusicBrainz](https://musicbrainz.org/)の中で，
アーティストに関するものをJSON形式に変換し，gzip形式で圧縮したファイルである．
このファイルには，1アーティストに関する情報が1行にJSON形式で格納されている．<br/>
An open music database [MusicBrainz](https://musicbrainz.org/),
that converts artist-related data into JSON format and compresses it in gzip format
as [artist.json.gz](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz).
In this file, information about one artist is stored in one line in JSON format. <br/>
开放式音乐数据库[MusicBrainz](https://musicbrainz.org/)将与艺术家相关的数据转换为JSON格式，
并将其压缩为gzip格式。
在[artist.json.gz](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz)文件中，
有关一位艺术家的信息以JSON格式存储在一行中。

artist.json.gzのデータをKey-Value-Store (KVS) およびドキュメント志向型データベースに
格納・検索することを考える．
KVSとしては，[LevelDB](http://leveldb.org/)，[Redis](http://redis.io/)，
[KyotoCabinet](http://rethinkdb.com/)等を用いよ．
ドキュメント志向型データベースとして，MongoDBを採用したが，CouchDBやRethinkDB等を用いてもよい．<br/>
Consider storing and searching artist.json.gz data in Key-Value-Store (KVS) and a document-oriented database.
Use [LevelDB](http://leveldb.org/),
[Redis](http://redis.io/),
[KyotoCabinet](http://fallabs.com/kyotocabinet/), etc. as KVS.
[MongoDB](http://www.mongodb.org/) was adopted as the document-oriented database,
but [CouchDB](http://couchdb.apache.org/), [RethinkDB](), etc. may be used.<br/>
尝试在键值存储（KVS）和面向文档的数据库中存储和搜索artist.json.gz数据。
将[LevelDB](http://leveldb.org/)，
[Redis](http://redis.io/)，
[KyotoCabinet](http://fallabs.com/kyotocabinet/)等用作KVS。
[MongoDB](http://www.mongodb.org/)可用作面向文档的数据库，
但也可以使用[CouchDB](http://couchdb.apache.org/)，
[RethinkDB](http://rethinkdb.com/)等。

### 60. KVSの構築
Building KVS<br/>
建立KVS

Key-Value-Store (KVS) を用い，
アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
Use Key-Value-Store (KVS) to construct a database
for searching the activity area (area) from the artist name (name).<br/>
使用键值存储（KVS）来构建数据库，
以便从艺术家姓名（名称）中搜索活动区域（区域）。

### 61. KVSの検索
Search in KVS<br/>
搜索KVS

60で構築したデータベースを用い，
特定の（指定された）アーティストの活動場所を取得せよ．<br/>
Using the database constructed in step 60,
obtain the activity location of a specific (designated) artist.<br/>
使用在步骤60中构建的数据库，
获取特定（指定）艺术家的活动位置。


### 62. KVS内の反復処理
Iterative processing in KVS<br/>
KVS中的迭代处理

60で構築したデータベースを用い，
活動場所が「Japan」となっているアーティスト数を求めよ．<br/>
Using the database constructed in 60,
find the number of artists whose activity place is "Japan".<br/>
使用在步骤60建立的数据库，找到活动地点为“日本”的艺术家数量。

### 63. オブジェクトを値に格納したKVS
KVS with object stored in value<br/>
将对象存储在KVS的值中

KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを
検索するためのデータベースを構築せよ．
さらに，ここで構築したデータベースを用い，
アーティスト名からタグと被タグ数を検索せよ．<br/>
Using KVS, build a database to search
for a list of tags and the number of tags (number of times they were tagged) from the artist name.
Using the database constructed here,
search for tags and the number of tags by artist name.<br/>
使用KVS，建立一个数据库，根据艺术家姓名搜索标签列表和标签数量（被标记的次数）。
使用此处构建的数据库，按艺术家名称搜索标签和标签数量。

### 64. MongoDBの構築
Build MongoDB<br/>
构建MongoDB

アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value<br/>
Register artist information (artist.json.gz) in the database.
In addition, index on the following fields: name, aliases.name, tags.value, rating.value<br/>
在数据库中注册艺术家信息（artist.json.gz）。
此外，在以下字段上建立索引：名称，aliases.name，tags.value，rating.value

### 65. MongoDBの検索
Search MongoDB<br/>
搜索MongoDB

MongoDBのインタラクティブシェルを用いて，
"Queen"というアーティストに関する情報を取得せよ．
さらに，これと同様の処理を行うプログラムを実装せよ．<br/>
Use MongoDB's interactive shell to get information about the artist "Queen".
In addition, implement a program that performs the same processing.<br/>
使用MongoDB的交互式Shell获取有关艺术家“Queen”的信息。
另外，实现可以执行相同处理的程序。

### 66. 検索件数の取得
Get search count<br/>
获取搜索计数

MongoDBのインタラクティブシェルを用いて，
活動場所が「Japan」となっているアーティスト数を求めよ．<br/>
Using MongoDB's interactive shell,
find the number of artists whose activity location is "Japan".<br/>
使用MongoDB的交互式Shell，查找活动位置为“日本”的艺术家数量。

### 67. 複数のドキュメントの取得
Retrieve multiple documents<br/>
检索多个文件

特定の（指定した）別名を持つアーティストを検索せよ．
Search for artists with a specific (specified) alias.<br/>
搜索具有特定（指定）别名的艺术家。

### 68. ソート
Sort<br>
排序

"dance"というタグを付与されたアーティストの中で
レーティングの投票数が多いアーティスト・トップ10を求めよ．<br/>
Find the top 10 artists with the highest number of votes among the artists tagged "dance".<br/>
在标记为“舞蹈”的艺术家中找到投票数最高的前10位艺术家。

### 69. Webアプリケーションの作成
Creating a web application<br/>
创建一个Web应用程序

ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．
アーティスト名，アーティストの別名，タグ等で検索条件を指定し，
アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．<br/>
Create a Web application that displays the artist information
that matches the search conditions entered by the user.
Specify search conditions by artist name, artist alias, tag, etc.,
and arrange the artist information list in order of highest rating.<br/>
创建一个显示与用户输入的搜索条件匹配的艺术家信息的Web应用。
通过艺术家名称，艺术家别名，标签等指定搜索条件，
并按等级降序对艺术家信息列表进行排序和显示。

## 第8章: 機械学習
本章では，Bo Pang氏とLillian Lee氏が公開している
[Movie Review Dat](http://www.cs.cornell.edu/people/pabo/movie-review-data/)の
[sentence polarity dataset v1.0](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt)を用い，
文を肯定的（ポジティブ）もしくは否定的（ネガティブ）に分類するタスク（極性分析）に取り組む．<br/>
In this chapter, using the 
[sentence polarity dataset v1.0](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt) of the 
[Movie Review Dat](http://www.cs.cornell.edu/people/pabo/movie-review-data/) published by Bo Pang and Lillian Lee, 
work on the described task (polarity analysis) of classifying sentences as positive (positive) or negative (negative).<br/>
在本章中，使用Bo Pang和Lillian Lee发行的 
[Movie Review Dat](http://www.cs.cornell.edu/people/pabo/movie-review-data/) 的 
[sentence polarity dataset v1.0](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt)，
尽力完成将句子分类为正（positive）或负（negative）的任务（极性分析）。


### 70. データの入手・整形
Obtaining and shaping data<br/>
获取和整理数据

[文に関する極性分析の正解データ](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz)
を用い，
以下の要領で正解データ（sentiment.txt）を作成せよ．<br/>
Create correct answer data (sentiment.txt) using the 
[correct answer data from the polarity analysis for the sentence](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz) as follows.<br/>
使用如下[句子极性分析中的正确答案数据](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz)创建正确答案数据（sentiment.txt）。

- rt-polarity.posの各行の先頭に"+1 "という文字列を追加する
（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）<br/>
Add the string "+1" to the beginning of each line in rt-polarity.pos 
(polarity label "+1" followed by a space, followed by the positive sentence)<br>
将字符串“ +1”添加到rt-polarity.pos中每行的开头
（极性标签“ +1”，后跟一个空格，后跟肯定句的内容）
- rt-polarity.negの各行の先頭に"-1 "という文字列を追加する
（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）<br/>
Add a string "-1" to the beginning of each line of rt-polarity.neg
(Polarity label "-1" followed by a space, followed by the contents of the negative sentence.)<br/>
将字符串“ -1”添加到rt-polarity.neg中每行的开头
（极性标签“ -1”，后跟一个空格，后跟否定句的内容）

- 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，
正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．<br/>
Concatenate the contents of 1 and 2 above, 
and create a sentiment.txt that randomly rearranges the lines. 
Check the number of positive examples (positive sentences) and the number of negative examples (negative sentences).<br/>
结合上面1和2的内容，并创建一个sendiment.txt来随机重新排列各行，
检查肯定示例（肯定句）和否定示例（否定句）的数量。

### 71. ストップワード
Stop word<br/>
停用词

英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
それ以外は偽を返す関数を実装せよ．
さらに，その関数に対するテストを記述せよ．<br/>
Create a list of English stop words (stop list). 
Furthermore, implement a function that returns true if the word (character string) 
given in the argument is included in the stoplist, 
and returns false otherwise. Write a test for the function.<br/>
创建英语停用词列表。
此外，实现一个函数，如果参数中给定的单词（字符串）包含在停用词表中，则返回true，否则返回false。
为该功能编写一个测试。<br/>

### 72. 素性抽出
Feature extraction<br/>
特征提取

極性分析に有用そうな素性を各自で設計し，
学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．<br/>
Design features that are likely to be useful for polarity analysis, 
and extract features from training data. 
The minimum baseline for the feature would be to remove the stopwords from the review and to stem each word.<br/>
设计可能对极性分析有用的特征，并从训练数据中提取特征。
该功能的最低基准是从评论中删除停用词并阻止每个词。

### 73. 学習
Learning<br/>
学习

72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．<br/>
Train a logistic regression model using the features extracted in 72.<br/>
使用72中提取的特征训练逻辑回归模型。

### 74. 予測
Predict<br/>
预测

73で学習したロジスティック回帰モデルを用い，
与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．<br/>
Using the logistic regression model learned in step 73, 
implement a program to calculate the polarity label 
of the given sentence ("+1" for positive examples, "-1" for negative examples) and its predicted probability.<br/>
使用在步骤73中训练的逻辑回归模型，
实现一个程序来计算给定句子的极性标签（对于肯定示例，“ + 1”，对于否定示例，“-1”）及其预测概率。

### 75. 素性の重み
Feature weight<br/>
特征权重

73で学習したロジスティック回帰モデルの中で，
重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．<br/>
In the logistic regression model learned in 73, 
check the top 10 features with high weight and the top 10 features with low weight.<br/>
在73训练的逻辑回归模型中，
检查权重较高的前10个特征和权重较低的前10个特征。

### 76. ラベル付け
Labeling<br/>
标注

学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．<br/>
Apply a logistic regression model to the training data and output the correct labels, 
predicted labels, and predicted probabilities in tab-delimited format.<br/>
将逻辑回归模型应用于训练数据，并以制表符分隔的格式输出正确的标签，预测的标签和预测正确的概率。

### 77. 正解率の計測
Measurement of accuracy rate<br/>
准确率的测量

76の出力を受け取り，
予測の正解率，正例に関する適合率，再現率，
F1スコアを求めるプログラムを作成せよ．<br/>
Write a program that receives the output of 76 and calculates the correct answer rate of the prediction, 
the precision rate for the correct example, the recall rate, and the F1 score.<br/>
编写一个程序，接收76的输出，并计算预测的准确率，精确率，召回率和F1分数。

### 78. 5分割交差検定
5-fold cross validation<br/>
5-fold交叉验证

76-77の実験では，学習に用いた事例を評価にも用いたため，
正当な評価とは言えない．
すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，
モデルの汎化性能を測定していない．
そこで，5分割交差検定により，
極性分類の正解率，適合率，再現率，F1スコアを求めよ．<br/>
In the experiment of 76-77, 
the case used for learning was also used for evaluation, 
so it cannot be said that it is a valid evaluation. 
In other words, the classifier evaluates the performance 
of memorizing the training examples 
and does not measure the generalization performance of the model. 
Therefore, calculate the correct answer rate, 
precision rate, recall rate, and F1 score 
of the polarity classification using 5-fold cross validation.<br/>
在76-77的实验中，用于学习的案例也用于评估，因此不能说这是有效的评估。
换句话说，分类器评估记忆训练样本的性能，而不衡量模型的泛化性能。
因此，使用5-fold交叉验证来计算极性分类的准确率，精确率，召回率和F1分数。

### 79. 適合率-再現率グラフの描画
Drawing Precision-Recall graph<br/>
绘制准确率-召回率图

ロジスティック回帰モデルの分類の閾値を変化させることで，
適合率-再現率グラフを描画せよ．<br/>
Draw a precision-recall graph by changing the classification threshold of the logistic regression model.<br/>
绘制精确率-召回率随逻辑回归模型的分类阀值变化图。

## 第9章: ベクトル空間法 (I)
Vector space method<br/>
向量空间法

[enwiki-20150112-400-r10-105752.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2)は，
2015年1月12日時点の英語のWikipedia記事のうち，
約400語以上で構成される記事の中から，
ランダムに1/10サンプリングした105,752記事のテキストをbzip2形式で圧縮したものである．
このテキストをコーパスとして，単語の意味を表すベクトル（分散表現）を学習したい．
第9章の前半では，コーパスから作成した単語文脈共起行列に主成分分析を適用し，
単語ベクトルを学習する過程を，いくつかの処理に分けて実装する．
第9章の後半では，学習で得られた単語ベクトル（300次元）を用い，
単語の類似度計算やアナロジー（類推）を行う．<br/>
[enwiki-20150112-400-r10-105752.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2) 
is a random sample of 1/10 of the English-language Wikipedia articles as of January 12, 2015, 
which consist of more than 400 words. 
This is the text of 105,752 articles compressed in bzip2 format. 
Using this text as a corpus, 
train a vector (distributed expression) that represents the meaning of a word. 
In the first half of Chapter 9, 
the process of learning word vectors 
by applying principal component analysis to the word context co-occurrence matrix 
created from the corpus is implemented in several processes. 
In the second half of Chapter 9, 
word similarity calculation and analogy (analog) are performed using word vectors (300 dimensions) 
obtained by learning.<br/>
[enwiki-20150112-400-r10-105752.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2)
是截至2015年1月12日的英语Wikipedia文章中的1/10个样本的随机样本，
文章包含约400或更多个单词。
一共105,752条以bzip2格式压缩的文章的文本。
使用这些文本作为语料库，训练一个代表单词含义的向量（分布式表达式）。
在第9章的前半部分中，
通过将主成分分析应用于从语料库创建的单词上下文共现矩阵来训练单词向量的过程
分为几个步骤实现。
在第9章的后半部分，使用训练获得的单词向量（300维）执行单词相似度计算和类比（模拟）。

なお，問題83を素直に実装すると，大量（約7GB）の主記憶が必要になる. 
メモリが不足する場合は，処理を工夫するか，
1/100サンプリングのコーパス
[enwiki-20150112-400-r100-10576.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r100-10576.txt.bz2)を用いよ．<br/>
If problem 83 is implemented straightforwardly, 
a large amount (about 7GB) of main memory will be required. 
If the memory is insufficient, 
devise the processing or use the corpus [enwiki-20150112-400-r100-10576.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r100-10576.txt.bz2) 
with 1/100 sampling.<br/>
如果直接开展步骤83，会用到大量（大约7GB）的内存。
如果内存不足，请先进行处理或使用1/100采样的语料库
[enwiki-20150112-400-r100-10576.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r100-10576.txt.bz2)。

### 80. コーパスの整形
Corpus shaping<br/>
语料库整形

文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである． 
ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう． 
そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，
各トークンに以下の処理を施し，単語から記号を除去せよ．
<br/>
The simplest way to convert a sentence into a sequence of words is to break it into words with space.
However, with this method, marks such as periods and parentheses 
at the end of the sentence are included in the word. 
So, after dividing the text of each line of the corpus into a list of tokens with blank characters, 
perform the following processing on each token to remove marks from words.<br/>
将句子转换为词序列最简单的方法是将其分解为带有空格的词。
但是，使用这种方法，会产生末尾附带句点和括号之类记号的词。
因此，在将语料库的每一行文本划分为带有空格字符的标记列表之后，
对每个标记执行以下处理以便从单词中去除记号。

- トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"<br/>
Remove the following characters at the beginning and end of the token: .,!?;: () [] '"<br/>
删除词例开头和结尾的以下字符： .,!?;: () [] '"

- 空文字列となったトークンは削除<br/>
Empty tokens are deleted<br/>
空词例需被删除

以上の処理を適用した後，
トークンをスペースで連結してファイルに保存せよ．<br/>
After applying processing above, 
connect the tokens with spaces and save them to a file.<br/>
上述处理后，用空格连接词例并将其保存在文件中。

### 81. 複合語からなる国名への対処
Dealing with compound word as country's name<br/>
处理复合词组成的国家名称

英語では，複数の語の連接が意味を成すことがある．
例えば，アメリカ合衆国は"United States"，
イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，
指し示している概念・実体が曖昧である．
そこで，コーパス中に含まれる複合語を認識し，
複合語を1語として扱うことで，複合語の意味を推定したい．
しかしながら，
複合語を正確に認定するのは大変むずかしいので，
ここでは複合語からなる国名を認定したい．<br/>
In English, concatenation of multiple words can make sense. 
For example, the America is represented as "United States" 
and the Britain as "United Kingdom", 
but the words "United", "States", and "Kingdom" alone are ambiguous. 
Therefore, we want to estimate the meaning of a compound word 
by recognizing the compound word contained in the corpus 
and treating the compound word as one word. 
However, it is very difficult to accurately recognize compound words, 
so here we want to recognize country names consisting of compound words.<br/>
在英语中，串联起来的多个单词可以是有意义的。
例如，美国被表示为“United States”，英国被表示为“United Kingdom”，
但是仅仅作为单词的“United”，“States”和“Kingdom”是含混的。
因此，我们希望通过识别语料库中包含的复合词
并将复合词视为一个词来估计复合词的含义。
但是，复合词很难被准确识别，
因此这里我们仅识别由复合词组成的国家/地区名称。

インターネット上から国名リストを各自で入手し，
80のコーパス中に出現する複合語の国名に関して，
スペースをアンダーバーに置換せよ．
例えば，"United States"は"United_States"，
"Isle of Man"は"Isle_of_Man"になるはずである．<br/>
Obtain a list of country names on the Internet 
and replace spaces with underscores in compound words that appear in the 80 corpus. 
For example, "United States" should be "United_States" 
and "Isle of Man" should be "Isle_of_Man".<br/>
获取互联网上的国家/地区名称列表，
对出现在这80个语料库中的复合词，用下划线替换空格。
例如，"United States"为"United_States"，"Isle of Man"为"Isle_of_Man"。

### 82. 文脈の抽出
Context extraction<br/>
上下文提取

81で作成したコーパス中に出現するすべての単語tに関して，
単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
ただし，文脈語の定義は次の通りとする．<br/>
Write out all pairs of word t and context word c in tab-delimited format 
for all words t appearing in the corpus created in 81. 
The definition of the context word is as follows.<br/>
以制表符分隔的格式
对81中的语料库中出现的所有单词 t 写出所有单词对 t 和上下文单词 c。 
上下文词的定义如下。

- ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）<br/>
Extract d words before and after the word t as context word c 
(however, the context word does not include the word t itself)<br/>
提取单词t之前和之后的d个单词作为上下文单词c（但是，上下文单词不包括单词t本身）

- 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
Each time a word t is selected,
the context width d is randomly determined within the range of {1,2,3,4,5}.
每次选择单词t时，上下文宽度d在{1,2,3,4,5}范围内随机确定。

### 83. 単語／文脈の頻度の計測
Measuring word / context frequency<br/>
测量 词/上下文 频率

82の出力を利用し，以下の出現分布，および定数を求めよ．

- f(t,c) : 単語tと文脈語cの共起回数<br/>
Number of co-occurrences of word t and context words c
单词t和上下文单词c的共现次数

- f(t,∗) : 単語tの出現回数<br/>
Number of occurrences of word t<br/>
单词t的出现次数

- f(∗,c) : 文脈語cの出現回数<br/>
Number of occurrences of context words c<br/>
上下文词c的出现次数

- N : 単語と文脈語のペアの総出現回数<br/>
Total number of occurrences of word-context word pairs<br/>
词-上下文词 对的出现总数

### 84. 単語文脈行列の作成
Create word context matrix<br/>
创建单词上下文矩阵

83の出力を利用し，単語文脈行列Xを作成せよ．
ただし，行列Xの各要素Xtcは次のように定義する．<br/>
Create a word context matrix X using the output of 83. 
Where each element Xtc of the matrix X is defined as follows.<br/>
使用83的输出创建单词上下文矩阵X。
矩阵X的每个元素Xtc定义如下。

- f(t,c)≥10ならば，Xtc = PPMI(t,c) = max{log(N×f(t,c))/(f(t,∗)×f(∗,c)),0}
if f(t,c)≥10: Xtc = PPMI(t,c) = max{log(N×f(t,c))/(f(t,∗)×f(∗,c)),0}

- f(t,c)<10ならば，Xtc = 0
else: Xtc = 0

ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
なお，行列Xの行数・列数は数百万オーダとなり，
行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
<br/>
Here, PPMI (t, c) is a statistic called Positive Pointwise Mutual Information. 
Note that the number of rows and columns of matrix X is on the order of several millions, 
and it is impossible to put all the elements of the matrix in main memory. 
Fortunately, most elements of matrix X are zero, so you only need to write out the nonzero elements.<br/>
在这里，PPMI(t，c)是一个统计量，称为正 点间互信息。 
请注意，矩阵X的行和列数约为数百万，
并且不可能将矩阵的所有元素都放在主存储器上。
所幸，矩阵X的大多数元素为零，因此您只需要写出非零元素。

### 85. 主成分分析による次元圧縮
Dimensional compression by principal component analysis<br/>
通过主成分分析进行尺寸压缩

84で得られた単語文脈行列に対して，主成分分析を適用し，
単語の意味ベクトルを300次元に圧縮せよ．<br/>
Apply principal component analysis to the word context matrix obtained in step 84, 
and compress the meaning vector of the word to 300 dimensions.
将主成分分析应用于在步骤84中获得的单词上下文矩阵，
并将单词语义向量压缩到300维。

### 86. 単語ベクトルの表示
Display word vector<br/>
显示单词向量

85で得た単語の意味ベクトルを読み込み，
"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．<br/>
Read the meaning vector of the word obtained in step 85 and display the "United States" vector.
Note that "United States" is internally represented as "United_States".<br/>
读取在步骤85中获得的词向量，并显示词"United States"。 注意，"United States"在内部表示为"United_States"。

### 87. 単語の類似度
Word similarity<br/>
单词相似度

85で得た単語の意味ベクトルを読み込み，
"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．<br/>
Read the semantic vector of the word obtained in step 85 and calculate the cosine similarity between "United States" and "U.S.". Note, however, that "U.S." is internally represented as "U.S."<br/>
读取在步骤85中获得的单词的词向量，并计算"United States"和"U.S."之间的余弦相似度。
但是请注意，"U.S."在内部表示为"U.S"。

### 88. 類似度の高い単語10件
10 words with high similarity<br/>
高度相似的10个词

85で得た単語の意味ベクトルを読み込み，
"England"とコサイン類似度が高い10語と，その類似度を出力せよ．<br/>
Read the semantic vector of the word obtained in step 85, 
and output 10 words with high cosine similarity to "England" and their similarity<br/>
读取在步骤85中获得的单词的词向量，
并输出与“England”具有高余弦相似度的10个单词及其相似度

### 89. 加法構成性によるアナロジー
Analogy with additive constructivity<br/>
类比与加法构造性

85で得た単語の意味ベクトルを読み込み，
vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．<br/>
Read the semantic vector of the word obtained in 85, 
calculate vec("Spain") - vec("Madrid") + vec("Athens"),
Output 10 words with high similarity to the vector and their similarity.<br/>
读取在85中获得的单词的向量，计算vec("Spain") - vec("Madrid") + vec("Athens")，
并输出10个与该向量最相似的词及其向量。

## 第10章: ベクトル空間法 (II)
Vector space method 02
向量空间法 其二

第10章では，
前章に引き続き単語ベクトルの学習に取り組む．<br/>
In Chapter 10, we will continue to learn word vectors 
as in the previous chapter.<br/>
在第10章中，我们将像上一章一样继续学习单词向量。

### 90. word2vecによる学習
Learning with word2vec<br/>
用word2vec学习

81で作成したコーパスに対して[word2vec](https://code.google.com/p/word2vec/)を適用し，
単語ベクトルを学習せよ．
さらに，学習した単語ベクトルの形式を変換し，
86-89のプログラムを動かせ．<br/>
Apply [word2vec](https://code.google.com/p/word2vec/) to the corpus 
created in step 81 to learn word vectors. 
Then, convert the learned word vector format and run the program from 86-89.<br/>
将[word2vec](https://code.google.com/p/word2vec/)应用于在步骤81中创建的语料库以学习单词向量。 
然后，转换训练得到的单词矢量格式并进行86-89的任务。

### 91. アナロジーデータの準備
Preparation of analogy data<br/>
准备类比数据

[単語アナロジーの評価データ](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/stuffs_91/questions-words.txt)
をダウンロードせよ．
このデータ中で": "で始まる行はセクション名を表す．
例えば，
": capital-common-countries"という行は，
"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，
"family"というセクションに含まれる評価事例を
抜き出してファイルに保存せよ．<br/>
Download the [word analogy evaluation data](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/stuffs_91/questions-words.txt)
Lines starting with ":" in this data represent section names. 
For example, 
the line ": capital-common-countries" marks the beginning 
of a section called "capital-common-countries". 
From the downloaded evaluation data, 
extract the evaluation examples included in the section "family" 
and save them to a file.<br/>
下载[单词类比评估数据](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/stuffs_91/questions-words.txt)
此数据中以":"开头的行表示节名称。 
例如，行": capital-common-countries"标记了
名为"capital-common-countries"的部分的开头。 
从下载的评估数据中，提取"family"部分中包含的评估示例，
并将其保存到文件中。

### 92. アナロジーデータへの適用
Application to analogy data<br/>
应用类比数据

91で作成した評価データの各事例に対して，
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，
その類似度を求めよ．
求めた単語と類似度は，
各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，
90で作成した単語ベクトルに対して適用せよ．<br/>
For each case in the evaluation data created in 91, 
calculate 
vec(word in the second column) - vec(word in the first column) + vec(word in the third column), 
Find the word with the highest similarity to the vector and its similarity.
Add the word and similarity to the end of each case. 
Apply this program to the word vector created in 85 and the word vector created in 90.<br/>
对于步骤91中创建的评估数据中的每种情况，:1227

计算vec(第二列中的单词) - vec(第一列中的单词) + vec(第三列中的单词)，
查找与向量相似度最高的单词。
在每种情况的末尾添加单词和相似性。
将此程序应用于在85中创建的单词向量和在90中创建的单词向量。

### 93. アナロジータスクの正解率の計算
Calculating the accuracy rate of analogy tasks<br/>
计算类比任务的准确率

92で作ったデータを用い，
各モデルのアナロジータスクの正解率を求めよ．<br/>
Using the data created in 92, find the accuracy rate of analogy tasks for each model.<br/>
使用在92中创建的数据，找到每个模型的类比任务的准确率。

### 94. WordSimilarity-353での類似度計算
Similarity calculation with WordSimilarity-353<br/>
使用WordSimilarity-353进行相似度计算

[The WordSimilarity-353 Test Collection](http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.zip)
の評価データを入力とし，
1列目と2列目の単語の類似度を計算し，
各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，
90で作成した単語ベクトルに対して適用せよ．<br/>
Create a program that takes the evaluation data 
of [The WordSimilarity-353 Test Collection](http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.zip)
as input, 
calculates the similarity between words in the first and second columns, 
and adds a similarity value to the end of each line. 
Apply this program to the word vector 
created in 85 and the word vector created in 90.<br/>
创建一个程序，
将[The WordSimilarity-353 Test Collection](http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.zip)
作为输入，
计算第一列和第二列中单词之间的相似度，
并将相似度值添加到每行的末尾。 
将此程序应用于在85中创建的单词向量和在90中创建的单词向量。

### 95. WordSimilarity-353での評価
Evaluation by WordSimilarity-353<br/>
通过WordSimilarity-353进行的评估

94で作ったデータを用い，
各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．<br/>
Using the data created in step 94, 
calculate the Spearman correlation coefficient 
between the ranking of similarity output from each model 
and the ranking of human similarity determination.<br/>
使用94中创建的数据，
对于每个模型，
计算模型相似度和人类相似度判断之间的Spearman相关系数。

Spearman's rank correlation coefficient:

![fomula_spearman_coe](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/stuffs_95/Spearman'sRankCorrelationCoefficient.svg)

### 96. 国名に関するベクトルの抽出
Extract vector about country name<br/>
提取有关国名的向量

word2vecの学習結果から，
国名に関するベクトルのみを抜き出せ．<br/>
Extract only vectors related to country names 
from the learning results of word2vec.<br/>
从word2vec的学习结果中仅提取与国家名称有关的向量。

### 97. k-meansクラスタリング
k-means clustering<br/>
k均值聚类
96の単語ベクトルに対して，
k-meansクラスタリングをクラスタ数k=5
として実行せよ．<br/>
Perform k-means clustering on word vectors in step 96 with k = 5 clusters.<br/>
对步骤96中的词向量执行k = 5 均值聚类。

### 98. Ward法によるクラスタリング
Clustering by Ward method
Ward法聚类

96の単語ベクトルに対して，
Ward法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．<br/>
Perform hierarchical clustering using the Ward method on word vectors in step 96. 
Visualize the clustering result as a dendrogram.<br/>
使用Ward方法对步骤96的词向量执行分层聚类。 
将聚类结果可视化为树状图。

### 99. t-SNEによる可視化
Visualization with t-SNE
使用t-SNE进行可视化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．<br/>
Visualize the vector space with t-SNE for word vectors in step 96.<br/>
使用t-SNE可视化步骤96的单词向量的向量空间。

