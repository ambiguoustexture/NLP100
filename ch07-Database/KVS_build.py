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
