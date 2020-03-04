# Author：ambiguoustexture
# Date: 2020-03-04

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
