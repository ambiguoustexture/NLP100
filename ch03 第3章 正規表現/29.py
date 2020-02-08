import json
import re
import urllib.parse, urllib.request

def extract(title):
    with open(file) as file_current:
        for line in file_current:
            json_line = json.loads(line)
            if json_line['title'] == title:
                return json_line['text']

def clean(text):
    pattern_emphasis = re.compile(r' (\'{2,5}) (.*?) (\1) ', re.MULTILINE + re.VERBOSE)
    text = pattern_emphasis.sub(r'\2', text)

    pattern_interlink = re.compile(r' \[\[ (?: [^|] *? \|) *? ([^|]*?) \]\] ', re.MULTILINE + re.VERBOSE)
    text = pattern_interlink.sub(r'\1',text)

    pattern_language = re.compile(r' \{\{lang (?: [^|] *? \|) *? ([^|]*?) \}\} ', re.MULTILINE + re.VERBOSE)
    text = pattern_language.sub(r'\1', text)

    pattern_outerlink = re.compile(r' \[http:\/\/ (?: [^\s] *? \s) ? ([^]] *?) \] ', re.MULTILINE + re.VERBOSE)
    text = pattern_outerlink.sub(r'\1', text)

    pattern_br_ref = re.compile(r' < \/? [br | ref] [^>] *? > ', re.MULTILINE + re.VERBOSE)
    text = pattern_br_ref.sub('', text)

    return text

file = 'jawiki-country.json'
pattern_basic_information = re.compile(r' ^\{\{基礎情報.*?$ (.*?) ^\}\}$ ', re.MULTILINE + re.VERBOSE + re.DOTALL)
basic_information = pattern_basic_information.findall(extract('イギリス'))

pattern_fields = re.compile(r' ^\| (.+?) \s* = \s* (.+?) (?: (?= \n\|) | (?= \n$) ) ', re.MULTILINE + re.VERBOSE + re.DOTALL)
fields = pattern_fields.findall(basic_information[0])

res = {}
for field in fields:
    res[field[0]] = clean(field[1])

file_name = res['国旗画像']

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(file_name) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

request = urllib.request.Request(url)
connection = urllib.request.urlopen(request)
data = json.loads(connection.read().decode())

url_real = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url_real)
