# Author：ambiguoustexture
# Date: 2020-02-05
import re

pattern = re.compile(r'''
	^	# Head of line
	(	# Start capturing target group
	.*	# Zero or more arbitrary characters
	\[\[Category:
	.*	# Zero or more arbitrary characters
	\]\]
	.*	# Zero or more arbitrary characters
	)	# End of group
	$	# End of line
	''', re.MULTILINE + re.VERBOSE)
        # re.MULTILINE 
        # specifies the data to be searched for multiple lines.
        # Without this, ^ or $ will only match the beginning or end of the search target, 
        # and the newline in the middle will not be targeted.

        # re.VERBOSE 
        # is specified to put a comment in the middle of the regular expression. 
        # If this is specified, a comment will be inserted with #. 
        # However, when specifying a space or #, escape with a backslash is required.

file = open('./UK.txt')
lines = file.readlines()
file.close()

for line in lines:
    if re.match(pattern, line):
        print(line, end='')










