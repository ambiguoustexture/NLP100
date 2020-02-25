# Author：ambiguoustexture
# Date: 2020-02-25

import xml.etree.ElementTree as ET

file_parsed   = 'nlp.txt.xml'
root = ET.parse(file_parsed)

references = {}
for coreference in root.iterfind('./document/coreference/coreference'):
    reference = coreference.findtext('./mention[@representative="true"]/text')
    for mention in coreference.iterfind('./mention'):
         if mention.get('representative', 'false') == 'false':
             sentence_index = int(mention.findtext('sentence'))
             start          = int(mention.findtext('start'))
             end            = int(mention.findtext('end'))
             
             if not (sentence_index, start) in references:
                 references[(sentence_index, start)] = (end, sentence_index)

for sentence in root.iterfind('./document/sentences/sentence'):
    sentence_index = int(sentence.get('id'))
    remain = 0
    for token in sentence.iterfind('./tokens/token'):
        token_index = int(token.get('id'))

        if remain == 0 and (sentence_index, token_index) in references:
            (end, reference) = references[(sentence_index, token_index)]
            print('[', reference, '] (', end='')
            remain = end - token_index

        print(token.findtext('word'), end='')

        if remain > 0:
            remain -= 1
            if remain == 0:
                print(')', end='')
        print(' ', end='')
    print()

