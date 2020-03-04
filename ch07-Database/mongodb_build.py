# Author：ambiguoustexture
# Date: 2020-03-04

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
