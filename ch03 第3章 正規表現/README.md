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
pattern = re.compile(r'''
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
pattern = re.compile(r'''
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
pattern = re.compile(r'''
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
    res = pattern.findall(text)
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
pattern = re.compile(r'''
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

### 26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

### 27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

### 28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

### 29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

