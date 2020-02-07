# Author：ambiguoustexture
# Date: 2020-02-06

import re

pattern_section_name = re.compile(r'''
        ^       # Head of line
        (={2,}) # Capture target, two or more '='
        \s*     # Zero or more extra whitespace
                # removed because there are extra whitespace before and after 'philosophy' and 'marriage'
        (.+?)   # Capture target, 0 or more arbitrary characters, 
                # non-greedy match
        \s*     # Extra zero or more blanks
        \1      # Back reference, same content as first capture target
        .*      # Zero or more arbitrary characters
        $       # End of line
        ''', re.MULTILINE + re.VERBOSE)

file = 'UK.txt'
with open(file) as text:
    text = text.read()
    res = pattern_section_name.findall(text)
    for line in res:
        level = len(line[0]) - 1
        print('{indent}{section}({level})'.format(
            indent='\t' * (level - 1), 
            section = line[1], 
            level = level))
