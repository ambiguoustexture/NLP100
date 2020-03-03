# Author：ambiguoustexture
# Date: 2020-03-03

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
