# Author：ambiguoustexture
# Date: 2020-02-07
import re

pattern_contents = re.compile(r'''
        ^\{\{基礎情報.*?$   # Line starting with '{{基礎情報'
        (.*?)               # Capture target,
                            # 0 or more arbitrary characters,
                            # non-greedy match
        ^\}\}$              # Line end with '}}'
        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

pattern_fields = re.compile(r'''
        ^\| 
        (.+?) 
        \s* 
        =
        \s* 
        (.+?)
        (?:         # Start ungrouped group 
        (?=\n\|)    # Before line feed + '|' (positive look-ahead) 
        | (?=\n$)   # Or line feed + before end (positive look-ahead) 
        )           # End of group
        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

pattern_remove_emphasis = re.compile(r'''
         \'{2,5}
         ''', re.MULTILINE + re.VERBOSE)

pattern_remove_interlink = re.compile(r'''
        \[\[        # Start with '[['
        (?:         # Start group not to be captured 
            [^|]*?  # 0 or more characters other than '|', non-greedy 
            \|      # '|'
        )??         # 0 or more characters other than '|', non-greedy
        ([^|]*?)    # Capture target, characters other than '|', non-greedy 
        \]\]        # End with ']]'
        ''', re.MULTILINE + re.VERBOSE)

file = 'UK.txt'

with open(file) as text:
    text = text.read()
    contents = pattern_contents.findall(text)
    fields = pattern_fields.findall(contents[0])

    res = {}
    keys = []
    for field in fields:
        res[field[0]] = pattern_remove_interlink.sub('', pattern_remove_emphasis.sub('', field[1]))
        keys.append(field[0])
    
    # use keys for confirmation
    for item in sorted(res.items(), 
            key = lambda field: keys.index(field[0])):
        print(item)
