# Author：ambiguoustexture
# Date: 2020-02-05

import json

file = 'jawiki-country.json'

with open(file) as file_current:
    for line in file_current:
        json_line = json.loads(line)
        if json_line['title'] == 'イギリス':
            print(json_line['text'])
            break
