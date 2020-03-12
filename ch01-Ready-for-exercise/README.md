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
```Python
# In Python Interective Shell

>>> str = "stressed"
>>> str = str[::-1]
>>> str
'desserts'
```

### 01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．<br/>
Take the 1st, 3rd, 5th, and 7th characters of the character string "パタトクカシーー" 
and obtain a concatenated character string.<br/>
取字符串“パタトクカシーー”的第1，第3，第5和第7个字符，以获得串联的字符串。

```Python
# In Python Interective Shell
>>> str = "パタトクカシーー"
>>> str[::2]
'タクシー'
```

### 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．<br/>
Obtain the character string "パタトクカシーー" 
by connecting the letters "パトカー" + "タクシー" alternately from the beginning.<br/>
通过从头开始交替连接字母“パトカー” +“タクシー”来获取字符串“パタトクカシーー”。
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
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．<br/>
Break the sentence 
"Now I need a drink, alcoholic course, after the heavy lectures involving quantum mechanics." 
into words, and make a list of the number of characters (in the alphabet) 
of each word in order of appearance.<br/>
把句子“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
分解为单词，
并创建一个列表，其中是从头开始按出现的顺序排列的每个单词的字符数（字母）。

```Python
# In Python Interective Shell
>>> str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
>>> str = str.split(' ')
>>> str_len = [len(word.rstrip('.,')) for word in str]
>>> print(str_len)
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
```

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
分解句子“Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
的第1、5、6、7、8、9、15、16、19 个单词的第一个字符，其他单词的前两个字符，
另外，对提取到的字符串和单词的位置（从头开始的单词次序）创建关联数组（字典或map类型）。
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
➜ python 04.py
['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mi', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca']
```

### 05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．<br/>
Create a function to get n-gram from a given sequence (string, list, etc.). 
Using this function, get the word bi-gram and character bi-gram 
from the sentence "I am an NLPer".<br/>
创建一个函数，根据给定的序列（字符串，列表等）得到n-gram。
使用此函数，从句子“I am a NLPer”中获取词bi-gram和字符bi-gram。

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
    print("letter based bi-gram of the sentence is\n:" + str(bi_gram_letter_based))
```
```Shell
➜ python n_gram.py
Sentence: I am an NLPer
Word based bi-gram of the sentence is:
{'i am': 1, 'am an': 1, 'an nlper': 1}
letter based bi-gram of the sentence is
:{'ia': 1, 'am': 1, 'ma': 1, 'an': 1, 'nn': 1, 'nl': 1, 'lp': 1, 'pe': 1, 'er': 1}
```

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
Sentence generation by template<br/>
通过模板生成句子

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．<br/>
Implement a function that accepts the arguments x, y, z 
and returns the string "x時のyはz". 
Check the execution result with x=12, y="気温", z=22.4.<br/>
实现一个接受参数x，y，z并返回字符串“z時のyはz”的函数。
用x=12, y="気温", z=22.4测试结果。

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
```Shell
➜ python cipher.py
I zn mlg zm NLPvi.
```
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
对于由空格分隔的单词序列，请创建一个程序，
该程序将字符保留在每个单词的开头和结尾，
并随机重新排列其他字符的顺序。 
但是，长度不超过4的单词不会重新排列。
对于一个适当的英语句子（例如，
“I couldn't believe that I could actually understand what I was reading : 
the phenomenal power of the human mind .”
）然后检查结果。
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
