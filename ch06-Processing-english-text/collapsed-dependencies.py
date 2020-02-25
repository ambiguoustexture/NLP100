import xml.etree.ElementTree as ET
import pydot_ng as pydot

file_parsed = './nlp.txt.xml'
root = ET.parse(file_parsed)


for sentence in root.iterfind('./document/sentences/sentence'):
    sentence_index = int(sentence.get('id'))

    edges = []
    for dependency in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
        if dependency.get('type') != 'punct':
            governor  = dependency.find('./governor')
            dependent = dependency.find('./dependent')
            edges.append((\
                    (governor.get('idx'), governor.text),\
                    (dependent.get('idx'), dependent.text)))

    if len(edges) > 0:
        tree =pydot.graph_from_edges(edges, directed=True)
        tree.write_png('./trees/{}.png'.format(sentence_index))
