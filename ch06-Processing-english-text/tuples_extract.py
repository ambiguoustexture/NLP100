# Author：ambiguoustexture
# Date: 2020-02-26

import xml.etree.ElementTree as ET
import pydot_ng as pydot

file_parsed = './nlp.txt.xml'
root = ET.parse(file_parsed)


for sentence in root.iterfind('./document/sentences/sentence'):
    sentence_index = int(sentence.get('id'))

    predicates, nsubjs, dobjs = {}, {}, {}
    for dependency in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
        dependency_type = dependency.get('type')
        if dependency_type == 'nsubj' or dependency_type == 'dobj':
            governor = dependency.find('./governor')
            index = governor.text
            predicates[index] = governor.text
            if dependency_type == 'nsubj':
                nsubjs[index] = dependency.find('./dependent').text
            else:
                dobjs[index] = dependency.find('./dependent').text
    for index, predicate in sorted(predicates.items(), key = lambda predicate: predicate[0]):
        nsubj = nsubjs.get(index)
        dobj  = dobjs.get(index)
        if nsubj is not None and dobj is not None:
            print(nsubj, '\t', predicate, '\t', dobj)
