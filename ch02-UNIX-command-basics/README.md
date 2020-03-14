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

```Python
# In Python Interective Shell
>>> f = open('hightemp.txt', 'r')
>>> print('number of lines: ', len(f.readlines()))
number of lines:  24
>>> f.close()
```
with *wc*
```Shell
➜ wc -l hightemp.txt
24 hightemp.txt
```

### 11. タブをスペースに置換
Replace tabs with spaces<br/>
用空格替换制表符

タブ1文字につきスペース1文字に置換せよ．確認には*sed*コマンド，*tr*コマンド，もしくは*expand*コマンドを用いよ．
Replace each tab with one space. Use the *sed* command, *tr* command, or *expand* command for confirmation.<br/>
将每个制表符替换为一个空格。 使用sed，tr 或 expand命令进行确认。
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

with *sed* but failed
```Shell
➜ sed 's/\t/ /g' hightemp.txt
```

with *tr*
```Shell
➜ tr '\t' ' ' < hightemp.txt
```

with *expand*
```Shell
➜ expand -t 1 hightemp.txt
```

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
with *cut*
```Shell
cut -f1 hightemp.txt > col1_cut.txt
cut -f2 hightemp.txt > col2_cut.txt
```

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

```Python
with open('col1.txt') as col1:
    col2 = open('col2.txt')
    res = open('col1&2.txt', 'w')

    for col1_line, col2_line in zip(col1, col2):
        res.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')
```
with *paste*
```Shell
➜ paste col1.txt col2.txt > col1\&2_paste.txt
➜ diff col1\&2.txt col1\&2_paste.txt
➜
```

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
高知県	江川崎	41      2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
```
with *head*
```Shell
➜ head -4 hightemp.txt
高知県	江川崎	41	    2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
```

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
Difference of the string in column<br/>
第一个字符串的差异

1列目の文字列の種類（異なる文字列の集合）を求めよ．確認には*sort*, *uniq*コマンドを用いよ．
Find the type of string in the first column (a set of different strings). 
Use the *sort* and *uniq* commands for confirmation.<br/>
找到第一列中字符串的（一个不同字符串的集合）种类。
使用*sort*和*uniq*命令进行确认。

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

```python
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

