# 100 Language Processing Knocks
Amateur practices and handmade codes in separate chapter folder.
The Internet and Search Engine help a lot.

## 第1章: 準備運動
### 00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
```Python
# In Python Interective Shell
>>> str = "stressed"
>>> str = str[::-1]
>>> str
'desserts'
```

### 01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
```Python
# In Python Interective Shell
>>> str = "パタトクカシーー"
>>> str[::2]
'タクシー'
```

### 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
```Python
# In Python Interective Shell
>>> str0 = "パトカー"
>>> str1 = "タクシー"
>>> res  = ""
>>> str(res)
>>> for i in range(len(str0)):
...     for j in range(len(str1)):
...             res += str0[i]
...             res += str1[i]
...             break
...
>>> res
'パタトクカシーー'
```

### 03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
```Python
# In Python Interective Shell
>>> str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
>>> str = str.split(' ')
>>> str_len = [len(word.rstrip('.,')) for word in str]
>>> print(str_len)
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
```

### 04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
```Python
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

str = str.split(" ")

res = []

for word, index in zip(str, range(len(str))):
    if index+1 in (1, 5, 6, 7, 8, 9, 15, 16, 19):
       res.append(word[0])
    else:
       res.append(word[0:2])

print(res)
```
```Shell
ch01 準備運動 git:(master) ✗ python 04.py
['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mi', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca']
```

### 05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
```Python
import re

def sequence_to_words(sequence):
    """clean the given sequence
    :param sequence:    given sequence (string, list, etc.)
    :return:            words in the sequence
    """
    sequence = re.sub('\n+', ' ', sequence).lower()
    words = re.split('\W+', sequence)

    return words

def get_n_gram(sequence, n, key):
    """naive implement of n-gram based on word or letter
    :param sequence:    given sequence (string, list, etc.)
    :param n:           n-gram for n=2
    :param key:         switch word based or letter based
                        "key = word" for word based
                        "key = letter" for letter based
    :return:            n-gram dictionary
    """
    words = sequence_to_words(sequence)
    if key == "word":
        n_gram_dic = {}
        for i in range(len(words) - n + 1):
            n_gram_current = " ".join(words[i:i + n])
            if n_gram_current not in n_gram_dic:
                n_gram_dic[n_gram_current] = 1
            else:
                n_gram_dic[n_gram_current] += 1

    elif key == "letter":
        str = ''.join(words)
        n_gram_dic = {}
        for i in range(len(str) - n + 1):
            n_gram_current = str[i:i + n]
            if n_gram_current not in n_gram_dic:
                n_gram_dic[n_gram_current] = 1
            else:
                n_gram_dic[n_gram_current] += 1

    return n_gram_dic

if __name__ == "__main__":
    # sequence = open("poem.txt").read()
    sequence = "I am an NLPer"
    bi_gram_word_based = get_n_gram(sequence, 2, key = "word")
    bi_gram_letter_based = get_n_gram(sequence, 2, key = "letter")
    print("Sentence: I am an NLPer")
    print("Word based bi-gram of the sentence is:\n" + str(bi_gram_word_based))
    print("letter based bi-gram of the sentence is:\n:" + str(bi_gram_letter_based))
```
```Shell
➜ python n_gram.py
Sentence: I am an NLPer
Word based bi-gram of the sentence is:
{'i am': 1, 'am an': 1, 'an nlper': 1}
letter based bi-gram of the sentence is:
{'ia': 1, 'am': 1, 'ma': 1, 'an': 1, 'nn': 1, 'nl': 1, 'lp': 1, 'pe': 1, 'er': 1}
```

### 06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
```Python
# In Python Interective Shell
>>> from n_gram import *
>>> str0 = "paraparaparadise"
>>> str1 = "paragraph"
>>> X = set(get_n_gram(str0, 2, key = "letter"))
>>> Y = set(get_n_gram(str1, 2, key = "letter"))
>>> X.union(Y)
{'ph', 'gr', 'pa', 'is', 'ar', 'ra', 'di', 'ap', 'se', 'ad', 'ag'}
>>> X.intersection(Y)
{'pa', 'ar', 'ap', 'ra'}
>>> X.difference(Y)
{'di', 'is', 'se', 'ad'}
>>> 'se' in X.union(Y)
True
```

### 07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
```Python
# In Python Interective Shell
>>> def func(x, y, z):
...     return str(x) + "時の" + str(y) + "は" + str(z)
...
>>> x, y, z = 12, '気温', 22.4
>>> print(func(x, y ,z))
12時の気温は22.4
```

### 08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
- その他の文字はそのまま出力
- この関数を用い，英語のメッセージを暗号化・復号化せよ．
```Python
def cipher (sequence):
    """replace with lowercase (219 - ascii of character)
    :param sequence:    given text
    :return:            encrypted text
    """
    sequence_list = []
    res = ''

    for i in range(len(sequence)):
        if sequence[i].islower():
            sequence_list.insert(i, chr(219 - ord(sequence[i])))
        else:
            sequence_list.insert(i, sequence[i])

    for i in range (len(sequence)):
        res += sequence_list[i]

    return res

if __name__ == "__main__":
    sequence = "I am not an NLPer."
    print(cipher(sequence))
```
```Python
➜ python cipher.py
I zn mlg zm NLPvi.
```

### 09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
```Python
import random

def typoglycemia(sequence):
    """
    Function that leaves the characters at the beginning and end of each word,
    and rearranges the order of the other characters randomly.
    However, words with a length of 4 or less are not rearranged.
    :param sequence:    given text
    :return:            rearranged text
    """
    words = sequence.split()

    for i in range(len(words)):
        if len(words[i]) > 4:
            word_partial = list(words[i][1:-1])
            random.shuffle(word_partial)
            word_shuffle = "".join(word_partial)
            words[i] = words[i][0] + word_shuffle + words[i][-1]

    return ' '.join(words)

if __name__ == "__main__":
    sequence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(sequence))
```
```Shell
➜ python 09.py
I clu'nodt belviee that I cluod alatcluy ursdtnnead what I was rednaig : the pemnnheoal peowr of the human mind .
```

## 第2章: UNIXコマンドの基礎

[hightemp.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt)は，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

### 10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
```Python
# In Python Interective Shell
>>> f = open('hightemp.txt', 'r')
>>> print('number of lines: ', len(f.readlines()))
number of lines:  24
>>> f.close()
```
```Shell
➜ wc -l hightemp.txt
24 hightemp.txt
```
### 11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
```Shell
# In Python Interective Shell
>>> f = 'hightemp.txt'
>>> with open(f) as text:
...     for line in text:
...             print(line.replace('\t', ' '), end = '')
...
高知県 江川崎 41 2013-08-12
埼玉県 熊谷 40.9 2007-08-16
愛知県 名古屋 39.9 1942-08-02
...
```

with sed **failed**
```Shell
➜ sed 's/\t/ /g' hightemp.txt
```

with tr successed
```Shell
➜ tr '\t' ' ' < hightemp.txt
```

with expand successed
```Shell
➜ expand -t 1 hightemp.txt
```

### 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
```Python
file = 'hightemp.txt'

with open(file) as text:
    col1 = open('col1.txt', 'w')
    col2 = open('col2.txt', 'w')

    for line in text:
        items = line.split('\t')
        col1.write(items[0] + '\n')
        col2.write(items[1] + '\n')
```

```Shell
cut -f1 hightemp.txt > col1_cut.txt
cut -f2 hightemp.txt > col2_cut.txt
```

### 13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
```Python
with open('col1.txt') as col1:
    col2 = open('col2.txt')
    res = open('col1&2.txt', 'w')

    for col1_line, col2_line in zip(col1, col2):
        res.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')
```
with paste
```Shell
➜ paste col1.txt col2.txt > col1\&2_paste.txt
➜ diff col1\&2.txt col1\&2_paste.txt
➜
```

### 14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
```Python
file = 'hightemp.txt'
n = int(input('N: '))

with open(file) as text:
    for index, line in enumerate(text):
        if index >= n:
            break
        print(line.rstrip())
```
```Shell
➜ python 14.py
N: 4
高知県	江川崎	41	    2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
```
with head
```Shell
➜ head -4 hightemp.txt
高知県	江川崎	41	    2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
```

### 15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
```Python
file = 'hightemp.txt'
n = int(input('N: '))

with open(file) as text:
    lines = text.readlines()

for line in lines[-n:]:
    print(line.rstrip())
```
```Shell
➜ python 15.py
N: 4
大阪府	豊中	39.9	1994-08-08
山梨県	大月	39.9	1990-07-19
山形県	鶴岡	39.9	1978-08-03
愛知県	名古屋	39.9	1942-08-02
```
with *tail*
```Shell
➜ tail -4 hightemp.txt
大阪府	豊中	39.9	1994-08-08
山梨県	大月	39.9	1990-07-19
山形県	鶴岡	39.9	1978-08-03
愛知県	名古屋	39.9	1942-08-02
```

### 16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
```Python
lines_count = len(lines)

for index, flag in enumerate(range(0, lines_count, n), 1):
    with open('hightemp_split_{:02d}.txt'.format(index), 'w') as split_file:
        for line in lines[flag:flag + n]:
            split_file.write(line)
```
```Shell
➜ python 16.py
N: 4
➜ ls
hightemp_split_01.txt
hightemp_split_02.txt
hightemp_split_03.txt
hightemp_split_04.txt
hightemp_split_05.txt
hightemp_split_06.txt
➜ diff hightemp_aa hightemp_split_01.txt
➜
```
with *split*
```Shell
➜ split -4 hightemp.txt hightemp_;ls

hightemp_aa
hightemp_ab
hightemp_ac
hightemp_ad
hightemp_ae
hightemp_af
```
### 17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
```Python
file = 'hightemp.txt'
with open(file) as text:
    items = set()
    for line in text:
        cols = line.split('\t')
        items.add(cols[0])

for item in items:
    print(item)
```
```Shell
➜ python 17.py
静岡県
千葉県
愛媛県
和歌山県
群馬県
高知県
大阪府
岐阜県
埼玉県
愛知県
山形県
山梨県
```
with *sort* & *uniq*
```Shell
➜ cut -f1 hightemp.txt | sort | uniq > hightemp_sort_uniq.txt
➜ python 17.py | sort | > hightemp_sort_uniq_without.txt;diff hightemp_sort_uniq_without.txt hightemp_sort_uniq.txt
➜ 
```

### 18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
```Python
file = 'hightemp.txt'
lines = open(file).readlines()
lines.sort(key = lambda line: float(line.split('\t')[2]), reverse = True)

for line in lines:
    print(line, end='')
    # there will be another blank line without "end=''"
```
with *sort*
```Shell
➜ sort -n -k 3 -r hightemp.txt
# -n   : sort by number
# -k 3 : sort by the 3rd col
# -r   : reverse
```

### 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
```Python
from itertools import groupby

file = 'hightemp.txt'
lines = open(file).readlines()
items = list(line.split('\t')[0] for line in lines)

items.sort()
res = [(item, len(list(group))) for item, group in groupby(items)]
res.sort(key = lambda item : item[1], reverse = True)

for item in res:
    print('{item}({count})'.format(item = item[0], count = item[1]))
```
with *cut* & *uniq* & *sort*
```Shell
➜ cut -f1 hightemp.txt | sort | uniq -c | sort -r
# -f1     : the 1st col
# uniq -c : make a set and count
# sort -r : sort reversely
```

## 第3章: 正規表現
Wikipediaの記事を以下のフォーマットで書き出したファイル[jawiki-country.json.gz](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz)がある．
- 1行に1記事の情報がJSON形式で格納される
- 各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
- ファイル全体はgzipで圧縮される
以下の処理を行うプログラムを作成せよ．

### 20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
```Python
import json

file = 'jawiki-country.json'

with open(file) as file_current:
    for line in file_current:
        json_line = json.loads(line)
        if json_line['title'] == 'イギリス':
            print(json_line['text'])
            break
```
```Shell
➜ python 20.py > UK.txt ; head UK.txt
{{redirect|UK}}
{{基礎情報 国
|略名 = イギリス
|日本語国名 = グレートブリテン及び北アイルランド連合王国
|公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>
*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>
*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>
*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>
*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>
```

### 21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
```Python
pattern_category = re.compile(r'''
        ^       # Head of line
        (       # Start capturing target group
        .*      # Zero or more arbitrary characters
        \[\[Category:
        .*      # Zero or more arbitrary characters
        \]\]
        .*      # Zero or more arbitrary characters
        )       # End of group
        $       # End of line
        ''', re.MULTILINE + re.VERBOSE)
        # re.MULTILINE
        # specifies the data to be searched for multiple lines.
        # Without this, ^ or $ will only match the beginning or end of the search target,
        # and the newline in the middle will not be targeted.

        # re.VERBOSE
        # is specified to put a comment in the middle of the regular expression.
        # If this is specified, a comment will be inserted with #.
        # However, when specifying a space or #, escape with a backslash is required.
```
```Shell
➜ python 21.py
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
...
```

### 22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
```Python
pattern_category_name = re.compile(r'''
        ^               # Head of line
        .*              # Zero or more arbitrary characters
        \[\[Category:
        (.*?)           # Capture target, 0 or more arbitrary characters, non-greedy match
        (?:\]\]|\|)     # Not captured, ']]' or '|'
        .*              # Zero or more arbitrary characters
        $               # End of line
        ''', re.MULTILINE + re.VERBOSE)
```
```Shell
➜ python 21.py
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
...
```

### 23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
```Python
pattern_section_name = re.compile(r'''
        ^       # Head of line
        (={2,}) # Capture target, two or more '='
        \s*     # Zero or more extra whitespace
                # removed because there are extra whitespace before and after 'philosophy' and 'marriage'
        (.+?)   # Capture target, 0 or more arbitrary characters,
                # non-greedy match
        \s*     # Extra zero or more blanks
        \1      # Back reference, same content as first capture target
        .*      # Zero or more arbitrary characters
        $       # End of line
        ''', re.MULTILINE + re.VERBOSE)

file = 'UK.txt'
with open(file) as text:
    text = text.read()
    res = pattern_section_name.findall(text)
    for line in res:
        level = len(line[0]) - 1
        print('{indent}{section}({level})'.format(
            indent='\t' * (level - 1),
            section = line[1],
            level = level))
```
```Shell
➜ python 23.py
国名(1)
歴史(1)
...
```
### 24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
```Python
pattern_file = re.compile(r'''
        (?:File|ファイル)   # Uncaptured, 'File' or 'ファイル'
        :
        (.+?)               # Capture target,
                            # 0 or more arbitrary characters,
                            # non-greedy match
        \|
        ''', re.VERBOSE)
```
```Shell
➜ python 24.py
Royal Coat of Arms of the United Kingdom.svg
Battle of Waterloo 1815.PNG
...
```
### 25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

Extract the field names and values of the "基礎情報" template included in the article 
and store them as dictionary objects.
```Python
pattern_contents = re.compile(r' ^\{\{基礎情報.*?$ (.*?) ^\}\}$', re.MULTILINE + re.VERBOSE + re.DOTALL)

pattern_fields = re.compile(r'^\| (.+?) \s* = \s* (.+?) (?: (?=\n\|) | (?=\n$) )', re.MULTILINE + re.VERBOSE + re.DOTALL)

file = 'UK.txt'

with open(file) as text:
    text = text.read()
    contents = pattern_contents.findall(text)
    fields = pattern_fields.findall(contents[0])

    res = {}
    keys = []
    for field in fields:
        res[field[0]] = field[1]
        keys.append(field[0])

    # use keys for confirmation in sorting
    for item in sorted(res.items(),
            key = lambda field: keys.index(field[0])):
        print(item)
```

### 26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

In Step 25, remove MediaWiki's emphasis markup (weak emphasis, emphasis, and strong emphasis) from the template value and convert it to text.

    weak emphasis       ''italics''
    emphasis            '''bold'''
    strong emphasis     '''''both'''''

```Python
pattern_emphasis = re.compile(r' \'{2,5}', re.MULTILINE + re.VERBOSE)
# use pattern.sub() to substitute emphasis markups
```
```Shell
➜ python 26.py > basic_information_without_emphasis.txt; diff basic_information_with_emphasis.txt basic_information_without_emphasis.txt
42c42
< ('確立形態4', "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更")
---
> ('確立形態4', '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更')
```

### 27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

In addition to the processing of 26, remove MediaWiki's internal link markup from the template value and convert it to text.

    MediaWiki's internal link markup        [[]]
```Python
pattern_interlink = re.compile(r' \[\[ (?:[^|]*?\|) ?? ([^|]*?) \]\] ', re.MULTILINE + re.VERBOSE)
# use pattern.sub() to substitute MediaWiki's internal link markups
```
```Shell
➜ python 27.py > basic_information_without_interlink.txt
➜ diff basic_information_without_emphasis.txt basic_information_without_interlink.txt

...
43,44c43,44
< ('確立年月日4', '[[1927年]]')
< ('通貨', '[[スターリング・ポンド|UKポンド]] (&pound;)')
---
> ('確立年月日4', '1927年')
> ('通貨', 'UKポンド (&pound;)')
49c49
< ('ccTLD', '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>')
---
> ('ccTLD', '.uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>')
```

### 28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

In addition to the processing of 27, remove MediaWiki markup from template values as much as possible, and format basic country information.

```Python
def clean(text):
    pattern_emphasis = re.compile(r' (\'{2,5}) (.*?) (\1) ', re.MULTILINE + re.VERBOSE)
    text = pattern_emphasis.sub(r'\2', text)

    pattern_interlink = re.compile(r' \[\[ (?: [^|] *? \|) *? ([^|]*?) \]\] ', re.MULTILINE + re.VERBOSE)
    text = pattern_interlink.sub(r'\1',text)

    pattern_language = re.compile(r' \{\{lang (?: [^|] *? \|) *? ([^|]*?) \}\} ', re.MULTILINE + re.VERBOSE)
    text = pattern_language.sub(r'\1', text)

    pattern_outerlink = re.compile(r' \[http:\/\/ (?: [^\s] *? \s) ? ([^]] *?) \] ', re.MULTILINE + re.VERBOSE)
    text = pattern_outerlink.sub(r'\1', text)

    pattern_br_ref = re.compile(r' < \/? [br | ref] [^>] *? > ', re.MULTILINE + re.VERBOSE)
    text = pattern_br_ref.sub('', text)

    return text
```

### 29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

Get the URL of the flag image using the contents of the template. (Hint: Call imageinfo of MediaWiki API to convert file references to URLs)
```Python
file_name = res['国旗画像']

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(file_name) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

request = urllib.request.Request(url)
connection = urllib.request.urlopen(request)
data = json.loads(connection.read().decode())

url_real = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url_real)
```
```Shell
➜ python 29.py
https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg
```
![UK flag](https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg)

## 第4章: 形態素解析
夏目漱石の小説『吾輩は猫である』の文章（[neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

Morphologically analyze the text of Soseki Natsume's novel "I am a cat" using MeCab, 
and save the results in a file called neko.txt.mecab. 
Use this file to implement a program that addresses the following questions.

なお，問題37, 38, 39は[matplotlib](http://matplotlib.org/)もしくは[Gnuplot](http://www.gnuplot.info/)を用いるとよい．

For problems 37, 38, and 39, use matplotlib or Gnuplot.

### 30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

Implement a program that reads the result of morphological analysis (neko.txt.mecab).
However, each morpheme is stored in a mapping type with the surface type (surface), basic type (base), part of speech (pos), and part of speech class 1 (pos1) as keys, and one sentence is represented as a list of morphemes (mapping type) Please.
Use the program you created here for the rest of Chapter 4.
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
動詞の表層形をすべて抽出せよ．

Extract all verb surface forms.
```Python
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
動詞の原形をすべて抽出せよ．

Extract all verb forms.
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
サ変接続の名詞をすべて抽出せよ．

Extract all nouns which verbs can be formed by adding "する" to.
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
2つの名詞が「の」で連結されている名詞句を抽出せよ．

Extract a noun phrase where two nouns are connected by "の".
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
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

Extract the concatenation of nouns (nouns that appear consecutively) with the longest match.
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
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

Find the words that appear in the text and their frequency of occurrence, and arrange them in descending order of frequency of appearance.
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
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

Display the 10 most frequently occurring words and their frequency of occurrence in a graph (eg a bar graph).
![bar graph](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch04%20形態素解析/ten_most_frequently_occurring_words.png)

### 38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

Draw a histogram of the frequency of occurrence of the word (the horizontal axis represents the frequency of appearance, and the vertical axis represents the number of types of words whose appearance frequency is represented by a bar graph).
![histrogram graph](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch04%20形態素解析/histogram.png)
### 39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

Plot a log-logarithmic graph with the frequency of occurrence of words on the horizontal axis and the frequency of occurrence on the vertical axis.
![zipf law](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch04%20形態素解析/zipf_law.png)

