# Author：ambiguoustexture
# Date: 2020-02-05

file = 'hightemp.txt'
lines = open(file).readlines()
lines.sort(key = lambda line: float(line.split('\t')[2]), reverse = True)

for line in lines:
    print(line, end='')
    # there will be another blank line without "end=''"
