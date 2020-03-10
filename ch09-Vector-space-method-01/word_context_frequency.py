# Author: ambiguoustexture
# Date: 2020-03-10

from collections import Counter
import pickle

file_context    = './context.txt'
file_counter_tc = './tc_counter'
file_counter_t  = './t_counter'
file_counter_c  = './c_counter'

tc_counter = Counter()
t_counter  = Counter()
c_counter  = Counter()

tc_current, t_current, c_current = [], [], []

with open(file_context) as context:
    for index, line in enumerate(context, start=1):
        line = line.strip()
        words = line.split('\t')
        tc_current.append(line)
        t_current.append(words[0])
        c_current.append(words[1])
        if index % 1000000 == 0:
           tc_counter.update(tc_current)
           t_counter.update(t_current)
           c_counter.update(c_current)
           tc_current, t_current, c_current = [], [], []

tc_counter.update(tc_current)
t_counter.update(t_current)
c_counter.update(c_current)

with open(file_counter_tc,  'wb') as tc:
    pickle.dump(tc_counter, tc)
with open(file_counter_t,   'wb') as t:
    pickle.dump(t_counter,  t)
with open(file_counter_c,   'wb') as c:
    pickle.dump(c_counter,  c)

print('N:', index)
