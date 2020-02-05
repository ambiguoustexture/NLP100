# Author：ambiguoustexture
# Date: 2020-02-05

file = 'hightemp.txt'
n = int(input('N: '))

with open(file) as text:
    lines = text.readlines()

for line in lines[-n:]:
    print(line.rstrip())
