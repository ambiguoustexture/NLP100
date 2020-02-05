# Author：ambiguoustexture
# Date: 2020-02-06

import re

pattern = re.compile(r'''
        (?:File|ファイル)   # Uncaptured, 'File' or 'ファイル'
        :
        (.+?)               # Capture target,
                            # 0 or more arbitrary characters,
                            # non-greedy match
        \|
        ''', re.VERBOSE)

file = 'UK.txt'
with open(file) as text:
    text = text.read()
    res = pattern.findall(text)
    for line in res:
        print(line)

