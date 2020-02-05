# Author：ambiguoustexture
# Date: 2020-02-05

file = 'hightemp.txt'
with open(file) as text:
    items = set()
    for line in text:
        cols = line.split('\t')
        items.add(cols[0])

for item in items:
    print(item)
