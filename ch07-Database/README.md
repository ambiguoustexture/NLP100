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
アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．<br/>
Use Key-Value-Store (KVS) to construct a database 
for searching the activity area (area) from the artist name (name).<br/>
使用键值存储（KVS）来构建数据库，
以便从艺术家姓名（名称）中搜索活动区域（区域）。
```python
# Author：ambiguoustexture
# Date: 2020-03-03

import gzip
import json
import leveldb

file_gz = './artist.json.gz'
file_db = './artist_db'

db = leveldb.LevelDB(file_db)

with gzip.open(file_gz, 'rt') as artists:
    for artist in artists:
        artist_json_line = json.loads(artist)
        # some artist has no name but id
        key = artist_json_line['name'] + '\t' + str(artist_json_line['id'])
        value = artist_json_line.get('area', '')
        db.Put(key.encode(), value.encode())

print('%d artists have been recored.' % len(list(db.RangeIter(include_value=False))))
```
```zsh
➜ python KVS_build.py
921337 artists have been recored.
```

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
