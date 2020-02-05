# Author：ambiguoustexture
# Date: 2020-02-05

file = 'hightemp.txt'
n = int(input('N: '))

with open(file) as text:
    lines = text.readlines()

lines_count = len(lines)

for index, flag in enumerate(range(0, lines_count, n), 1):
    with open('hightemp_split_{:02d}.txt'.format(index), 'w') as split_file:
        for line in lines[flag:flag + n]:
            split_file.write(line)
