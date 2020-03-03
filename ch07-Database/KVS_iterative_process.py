# Author：ambiguoustexture
# Date: 2020-03-03

import re
import leveldb

file_db = './artist_db'
db = leveldb.LevelDB(file_db)

res = [value[0].decode() for value in db.RangeIter() if value[1] == 'Japan'.encode()]
print('There are %s records in Japan.' % len(res))
