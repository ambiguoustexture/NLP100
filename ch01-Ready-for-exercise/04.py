# Author：ambiguoustexture
# Date:   2020-02-02

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

str = str.split(" ")

res = []

for word, index in zip(str, range(len(str))):
    if index+1 in (1, 5, 6, 7, 8, 9, 15, 16, 19):
       res.append(word[0])
    else:
       res.append(word[0:2])

print(res)
