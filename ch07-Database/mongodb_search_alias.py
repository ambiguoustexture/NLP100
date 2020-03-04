# Author：ambiguoustexture
# Date: 2020-03-04

import json
from pymongo import MongoClient
from bson.objectid import ObjectId 
from mongodb_search import support_ObjectId

client = MongoClient()
db = client.db_MusicBrainz
collection = db.artists

search_alias_clue = input('Please input the artist\'s alias: ')
for i, artist in enumerate(collection.find({'aliases.name': search_alias_clue}), start = 1):
        print('Record {}: \n{}'.format(i, json.dumps(\
                artist,\
                indent='\t',\
                ensure_ascii=False,\
                sort_keys=True,\
                default=support_ObjectId\
                )))
