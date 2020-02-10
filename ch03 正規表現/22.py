# Author：ambiguoustexture
# Date: 2020-02-06
import re

pattern_category_name = re.compile(r'''
	^		# Head of line
	.*		# Zero or more arbitrary characters
	\[\[Category:
	(.*?)	        # Capture target, 0 or more arbitrary characters, non-greedy match 
	(?:\]\]|\|)	# Not captured, ']]' or '|'
	.*		# Zero or more arbitrary characters
	$		# End of line
	''', re.MULTILINE + re.VERBOSE)

file = 'UK.txt'
with open(file) as text:
    text = text.read()
    res = pattern_category_name.findall(text)
    for line in res:
        print(line)




