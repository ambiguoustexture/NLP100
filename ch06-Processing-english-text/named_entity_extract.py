# Author：ambiguoustexture
# Date: 2020-02-25

import xml.etree.ElementTree as ET

file_parsed   = 'nlp.txt.xml'
root = ET.parse(file_parsed)
for token in root.iterfind('./document/sentences/sentence/tokens/token[NER="PERSON"]'):
    print(token.findtext('word'))
