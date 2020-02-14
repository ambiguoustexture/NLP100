# Author：ambiguoustexture
# Date: 2020-02-09
import re

pattern_contents = re.compile(r' ^\{\{基礎情報.*?$ (.*?) ^\}\}$', re.MULTILINE + re.VERBOSE + re.DOTALL)

pattern_fields = re.compile(r'^\| (.+?) \s* = \s* (.+?) (?: (?=\n\|) | (?=\n$) )', re.MULTILINE + re.VERBOSE + re.DOTALL)

file = 'UK.txt'

with open(file) as text:
    text = text.read()
    contents = pattern_contents.findall(text)
    fields = pattern_fields.findall(contents[0])

    res = {}
    keys = []
    for field in fields:
        res[field[0]] = field[1]
        keys.append(field[0])
        
    # use keys for confirmation in sorting
    for item in sorted(res.items(), 
            key = lambda field: keys.index(field[0])):
        print(item)
