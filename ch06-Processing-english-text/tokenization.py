# Author：ambiguoustexture
# Date: 2020-02-25

import os
import subprocess
import xml.etree.ElementTree as ET

file_original = 'nlp.txt'
file_parsed   = 'nlp.txt.xml'


def parse():
    if not os.path.exists(file_parsed):
        subprocess.run(
            'java -cp "/usr/local/lib/stanford-corenlp-full-2018-10-05/*"'
            ' -Xmx3g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + file_original + ' 2>parse.out',
            shell=True,
            check=True)

parse()
root = ET.parse(file_parsed)
for word in root.iter('word'):
    print(word.text)

