## 第3章: 正規表現
Regular Expression<br/>
正则表达式

Wikipediaの記事を以下のフォーマットで書き出したファイル<br/>
There is a file 
[jawiki-country.json.gz](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz)
 which is a Wikipedia article written in the following format.<br/>
[jawiki-country.json.gz](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz)がある.
有一个文件
[jawiki-country.json.gz](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz)
，它是维基百科的文章，格式如下。

- 1行に1記事の情報がJSON形式で格納される<br/>
Information of one article is stored in JSON format per line<br/>
每行一篇文章的信息以JSON格式存储

- 各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される<br/>
In each line, the article name is stored in the dictionary object with the key "title" and the body of the article in the key "text", and the object is written out in JSON format.<br/>
在每一行中，文章名称都存储在字典对象中，其关键字为“title”，文章的主体为关键字“ text”，并且该对象以JSON格式存储。

- ファイル全体はgzipで圧縮される以下の処理を行うプログラムを作成せよ．<br/>
The whole file is compressed with gzip. 
Create a program that performs the following processing.<br/>
整个文件使用gzip压缩，请创建一个程序来执行以下处理。

### 20. JSONデータの読み込み
Reading JSON data<br/>
读取JSON数据

Wikipedia記事のJSONファイルを読み込み，
「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．<br/>
Read the JSON file of the Wikipedia article and display the article text about "United Kingdom". 
In questions 21-29, process the article body extracted here.<br/>
读取Wikipedia文章的JSON文件，
并显示有关“ United Kingdom”的文章文本。
在问题21-29中，对此处提取的文章正文执行操作。

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
Extract rows containing category names<br/>
提取包含category名称的行

記事中でカテゴリ名を宣言している行を抽出せよ．<br/>
Extract the line that declares the category name in the article.<br/>
提取在文章中声明category名称的行。

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
Extract category name<br/>
提取类别名称

記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．<br/>
Extract the article category names (by name, not line by line).<br/>
提取文章类别名称（按名称，而不是逐行）。
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
Section structure<br/>
章节结构

記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．<br/>
Display the section name and its level included in the article (for example, 1 if "== section name ==").<br/>
显示文章中包含的章节名称及其级别（例如，如果"==节名称=="，则为1）。
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
Extract file references<br/>
提取文件引用

記事から参照されているメディアファイルをすべて抜き出せ．<br/>
Extract all media files referenced in the article.<br/>
提取本文中引用的所有媒体文件。

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
Extract template<br/>
提取模板

記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．<br/>
Extract the field names and values of the "基礎情報" template included in the article 
and store them as dictionary objects.
<br/>
提取文章中包含的“基本信息”模板的字段名称和内容，并将其存储为字典对象。

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
Remove emphasis markup<br/>
删除强调标记

25の処理時に，
テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去して
テキストに変換せよ（参考: マークアップ早見表）．<br/>
In Step 25, 
remove MediaWiki's emphasis markup (weak emphasis, emphasis, and strong emphasis) 
from the template value and convert it to text.<br/>
从模板的内容中删除MediaWiki强调标记（弱强调，强调，强强调），
并在处理25（参考：标记快速参考表）期间将其转换为文本。

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
Removal of internal links<br/>
删除内部链接

26の処理に加えて，
テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ（参考: マークアップ早見表）．<br/>
In addition to the processing of 26, 
remove MediaWiki's internal link markup from the template value and convert it to text.
<br/>
在步骤26之上，从模板内容中删除MediaWiki的内部链接标记，
并将其转换为文本（参考：快速参考标记）。

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
Remove MediaWiki markup<br/>
删除MediaWiki标记

27の処理に加えて，
テンプレートの値からMediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ．<br/>
In addition to the processing of 27, 
remove MediaWiki markup from template values as much as possible, 
and format basic country information.
<br/>
在步骤27之上，尽可能从模板值中删除MediaWiki标记，并调整基本国家/地区信息的格式。

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
Get URL of national flag image<br/>
获取国旗图片的URL

テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）<br/>
Get the URL of the flag image using the contents of the template. 
(Hint: Call imageinfo of MediaWiki API to convert file references to URLs)
<br/>
使用模板的内容获取国旗图像的URL。
（提示：调用MediaWiki API的imageinfo将文件引用转换为URL）

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

