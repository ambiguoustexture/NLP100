#!/Users/there/miniconda3/envs/NLP_Koncks/bin/python
# coding: utf-8
from string import Template
import pymongo
from pymongo import MongoClient
import cgi
import cgitb
from html import escape

cgitb.enable()

max_view_count = 20

template_html = Template('''
<html>
    <head>
        <title>Database MusicBrainz</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
            body{
                max-width:410px;
                padding: 10%;
                margin:0 auto;
                }
        </style>
    </head>
    <body>
        <form method="GET" action="/cgi-bin/main.py">
            Name or aliases：<br>
            <input type="text" name="name" value="$clue_name" size="20"/><br />
            Tag：<br>
            <input type="text" name="tag" value="$clue_tag" size="20"/><br />
            <input type="submit" value="Search"/>
        </form>
        $message
        $contents
    </body>
</html>
''')

template_result = Template('''
        <hr />
        Record $index of $total:<br />
        <li>Name:           $name   <br />
        <li>Aliases:        $aliases<br />
        <li>Activity area:  $area   <br />
        <li>Tags:           $tags   <br />
        <li>Rating:         $rating <br />
''')

client = MongoClient()
db = client.db_MusicBrainz
collection = db.artists

form = cgi.FieldStorage()
clue = {}
clue_name = ''
clue_tag = ''

if 'name' in form:
    clue_name = form['name'].value
    clue = {'$or': [{'name': clue_name}, {'aliases.name': clue_name}]}

if 'tag' in form:
    clue_tag = form['tag'].value
    if len(clue) > 0:
        clue = {'$and': [clue, {'tags.value': clue_tag}]}
    else:
        clue = {'tags.value': clue_tag}

contents = ''
total = -1
if len(clue) > 0:

    results = collection.find(clue)
    results.sort('rating.count', pymongo.DESCENDING)
    total = results.count()

    dict_template = {}
    for i, doc in enumerate(results[0:max_view_count], start=1):

        dict_template['index'] = i
        dict_template['total'] = total
        dict_template['name'] = escape(doc['name'])

        if 'aliases' in doc:
            dict_template['aliases'] = \
                ','.join(escape(alias['name']) for alias in doc['aliases'])
        else:
            dict_template['aliases'] = 'NONE'

        if 'area' in doc:
            dict_template['area'] = escape(doc['area'])
        else:
            dict_template['area'] = 'NONE'

        if 'tags' in doc:
            dict_template['tags'] = \
                ','.join(escape(tag['value']) for tag in doc['tags'])
        else:
            dict_template['tags'] = 'NONE'

        if 'rating' in doc:
            dict_template['rating'] = doc['rating']['count']
        else:
            dict_template['rating'] = 'NONE'

        contents += template_result.substitute(dict_template)

dict_template = {}
dict_template['clue_name'] = escape(clue_name)
dict_template['clue_tag'] = escape(clue_tag)
dict_template['contents'] = contents

if total > max_view_count:
    dict_template['message'] = 'Displaying the top {} items.'.format(max_view_count)
elif total == -1:
    dict_template['message'] = 'Please enter search clue.'
elif total == 0:
    dict_template['message'] = 'No matching artists found.'
else:
    dict_template['message'] = ''

print(template_html.substitute(dict_template))
