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
KVS搜索

60で構築したデータベースを用い，
特定の（指定された）アーティストの活動場所を取得せよ．<br/>
Using the database constructed in step 60, 
obtain the activity location of a specific (designated) artist.<br/>
使用在步骤60中构建的数据库，
获取特定（指定）艺术家的活动位置。
```python
import re
import leveldb

file_db = './artist_db'
db = leveldb.LevelDB(file_db)
key_pattern = re.compile(r' ^(.*) \t (\d+)$ ', re.VERBOSE + re.DOTALL)

clue = input('Please input the artist\'s name: ')

flag_hit = False
for key, value in db.RangeIter((clue + '\t').encode()):
    key_match   = key_pattern.match(key.decode())
    artist_name = key_match.group(1)
    aritst_id   = key_match.group(2)
    if artist_name != clue:
        break
    area = value.decode()
    if area != '':
        print('%s (id:' % artist_name, '%6' 's) ' % aritst_id, 'had activities in %s' % area)
    else :
        print('There is no record of the activity location of %s' % artist_name)
    flag_hit = True

if not flag_hit:
    print('There is no record of %s' % artist_name)
```
```zsh
➜ python KVS_search.py
Please input the artist's name: Muse
Muse (id: 238985)  had activities in United States
Muse (id: 238988)  had activities in France
Muse (id: 241100)  had activities in New Zealand
Muse (id:   2591)  had activities in United Kingdom
Muse (id: 266713)  had activities in Australia
```

### 62. KVS内の反復処理
Iterative processing in KVS<br/>
KVS中的迭代处理

60で構築したデータベースを用い，
活動場所が「Japan」となっているアーティスト数を求めよ．<br/>
Using the database constructed in 60, 
find the number of artists whose activity place is "Japan".<br/>
使用在步骤60建立的数据库，找到活动地点为“日本”的艺术家数量。
```python
import re
import leveldb

file_db = './artist_db'
db = leveldb.LevelDB(file_db)

res = [value[0].decode() for value in db.RangeIter() if value[1] == 'Japan'.encode()]
print('There are %s records in Japan.' % len(res))
```
```zsh
➜ python KVS_iterative_process.py
There are 22821 records in Japan.
```

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
```python
import re
import gzip
import json
import leveldb

file_gz = './artist.json.gz'
file_db = './artist_object_db'

try:
    db = leveldb.LevelDB(file_db, error_if_exists=True)
    with gzip.open(file_gz, 'rt') as artists:
        for artist in artists:
            artist_json_line = json.loads(artist)
            key = artist_json_line['name'] + '\t' + str(artist_json_line['id'])
            value = artist_json_line.get('tags')
            if value is None:
                value = []
            db.Put(key.encode(), json.dumps(value).encode())
    print('%d record have been recored.' % len(list(db.RangeIter(include_value=False))))
except:
    db = leveldb.LevelDB(file_db)
    print('Use existed DB.')

search_clue = input('Please input the artist\'s name: ')
flag_hit = False
key_pattern = re.compile(r' ^(.*) \t (\d+)$ ', re.VERBOSE + re.DOTALL)

for key, value in db.RangeIter((search_clue + '\t').encode()):
    key_match   = key_pattern.match(key.decode())
    artist_name = key_match.group(1)
    artist_id   = key_match.group(2)

    if artist_name != search_clue:
        break

    tags = json.loads(value.decode())
    print('Tags of %s (id:' % artist_name, '%6' 's) ' % artist_id)
    if len(tags) > 0:
        for tag in tags:
            print('\t', tag['value'], tag['count'])
    else :
        print('\t There is no tag.')
    flag_hit = True

if not flag_hit:
    print('There is no record of %s' % search_clue)
```
```zsh
Use existed DB.
Please input the artist's name: Muse
Tags of Muse (id: 238985)
	 There is no tag.
Tags of Muse (id: 238988)
	 There is no tag.
Tags of Muse (id: 241100)
	 There is no tag.
Tags of Muse (id:   2591)
	 english 1
	 uk 4
	 british 3
	 new prog 2
	 alternative rock 2
	 britannique 1
	 best 1
	 rock and indie 1
	 united kingdom 1
	 producteur 1
	 producer 1
	 progressive rock 1
	 rock 5
	 male 1
Tags of Muse (id: 266713)
	 There is no tag.
```
### 64. MongoDBの構築
Build MongoDB<br/>
构建MongoDB

アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value<br/>
Register artist information (artist.json.gz) in the database. 
In addition, index on the following fields: name, aliases.name, tags.value, rating.value<br/>
在数据库中注册艺术家信息（artist.json.gz）。 
此外，在以下字段上建立索引：name，aliases.name，tags.value，rating.value
```python
import gzip
import json
import pymongo
from pymongo import MongoClient

file_gz = './artist.json.gz'
unit_bulk = 10000

client = MongoClient()
db = client.db_MusicBrainz
collection = db.artists

with gzip.open(file_gz, 'rt') as artists:
    buf = []
    for i, artist in enumerate(artists, 1):
        artist_json_line = json.loads(artist)
        buf.append(artist_json_line)

        if i % unit_bulk == 0:
            collection.insert_many(buf)
            buf = []
            print('%d records have been recored.' % i)

    if len(buf) > 0:
        collection.insert_many(buf)
        print('%d records have been recored.' % i)


collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])
```
Start MongDB before running Python script.
```zsh
➜ mongod
2020-03-04T15:17:24.595+0800 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2020-03-04T15:17:24.604+0800 I CONTROL  [initandlisten] MongoDB starting : pid=28427 port=27017 dbpath=/data/db 64-bit host=here.local
...

```
```zsh
➜ python mongodb_build.py
10000  records have been recored.
20000  records have been recored.
30000  records have been recored.

...

870000 records have been recored.
880000 records have been recored.
890000 records have been recored.
900000 records have been recored.
910000 records have been recored.
920000 records have been recored.
921337 records have been recored.
```

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

In  Mongo shell:
```mongo
> show dbs
admin           0.000GB
config          0.000GB
db_MusicBrainz  0.135GB
local           0.000GB
> use db_MusicBrainz
switched to db db_MusicBrainz
> db.artists.find( { 'name': 'Queen' } );
{ "_id" : ObjectId("5e5f56367334d6ef4751d978"), "name" : "Queen", "area" : "Japan", "gender" : "Female", "tags" : [ { "count" : 1, "value" : "kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
{ "_id" : ObjectId("5e5f56387334d6ef4752a024"), "rating" : { "count" : 24, "value" : 92 }, "begin" : { "date" : 27, "month" : 6, "year" : 1970 }, "name" : "Queen", "area" : "United Kingdom", "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "sort_name" : "Queen", "ended" : true, "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "type" : "Group", "id" : 192, "aliases" : [ { "name" : "女王", "sort_name" : "女王" } ] }
{ "_id" : ObjectId("5e5f563b7334d6ef47545a7c"), "ended" : true, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen", "id" : 992994, "name" : "Queen" }
>
```
With python:
```python
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

def support_ObjectId(obj):
    """Since ObjectId cannot be json-encoded, convert it to a string type
    return: string converted from ObjectId
    """
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(repr(obj) + " is not JSON serializable")


client = MongoClient()
db = client.db_MusicBrainz
collection = db.artists

for i, artist in enumerate(collection.find({'name': 'Queen'}), start = 1):
    print('Record {}：\n{}'.format(i, json.dumps(\
            artist,\
            indent='\t', \
            ensure_ascii=False, \
            sort_keys=True,\
            default=support_ObjectId\
            )))
```
```zsh
➜ python mongodb_search.py > mongodb_search_Queen.txt; head -32 mongodb_search_Queen.txt
Record 1：
{
	"_id": "5e5f56367334d6ef4751d978",
	"aliases": [
		{
			"name": "Queen",
			"sort_name": "Queen"
		}
	],
	"area": "Japan",
	"ended": true,
	"gender": "Female",
	"gid": "420ca290-76c5-41af-999e-564d7c71f1a7",
	"id": 701492,
	"name": "Queen",
	"sort_name": "Queen",
	"tags": [
		{
			"count": 1,
			"value": "kamen rider w"
		},
		{
			"count": 1,
			"value": "related-akb48"
		}
	],
	"type": "Character"
}
Record 2：
{
	"_id": "5e5f56387334d6ef4752a024",
	"aliases": [
```

### 66. 検索件数の取得
Get search count<br/>
获取搜索计数

MongoDBのインタラクティブシェルを用いて，
活動場所が「Japan」となっているアーティスト数を求めよ．<br/>
Using MongoDB's interactive shell, 
find the number of artists whose activity location is "Japan".<br/>
使用MongoDB的交互式Shell，查找活动位置为“日本”的艺术家数量。
```mongodb
> show dbs
admin           0.000GB
config          0.000GB
db_MusicBrainz  0.135GB
local           0.000GB
> use db_MusicBrainz
switched to db db_MusicBrainz
> db.artists.find({'area': 'Japan'}).count()
22821
```

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
