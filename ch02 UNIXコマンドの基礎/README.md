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
```Python
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

### 16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

### 17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

### 18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

### 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
