# Author：ambiguoustexture
# Date: 2020-02-05

from itertools import groupby

file = 'hightemp.txt'
lines = open(file).readlines()
items = list(line.split('\t')[0] for line in lines)

items.sort() 
res = [(item, len(list(group))) for item, group in groupby(items)]
res.sort(key = lambda item : item[1], reverse = True)

for item in res:
    print('{item}({count})'.format(item = item[0], count = item[1]))

