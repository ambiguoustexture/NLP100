# 100 Language Processing Knocks
Amateur practices and handmade codes in separate chapter folder.
Mr.[segavvy](https://qiita.com/segavvy)'s posts on [qiita](https://qiita.com) and internet help a lot. Thanks!
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
```Python
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
    with open('hightemp_split_{:02d}.txt'.format(index), 'w') as split_file:        for line in lines[flag:flag + n]:
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
