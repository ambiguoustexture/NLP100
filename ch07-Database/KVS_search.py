# Author：ambiguoustexture
# Date: 2020-03-03

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
