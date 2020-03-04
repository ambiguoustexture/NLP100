# Author：ambiguoustexture
# Date: 2020-03-04

import json
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.db_MusicBrainz
collection = db.artists 

res = collection.find({'tags.value' : 'dance'})

res.sort('rating.count', pymongo.DESCENDING)

for artist in res.limit(10):
    if 'rating' in artist:
        rating = artist['rating']['count']
    else :
        rating = '(none)'

    print(artist['name'].ljust(16, ' '), '(id: ', str(artist['id']).ljust(6, ' '), ')\t', rating)
