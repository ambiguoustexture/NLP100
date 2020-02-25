# Author：ambiguoustexture
# Date: 2020-02-26

from nltk.tree import Tree
import xml.etree.ElementTree as ET

def s_expression_analysis(tree):
    np_list = []
    root = tree.getroot()
    for parse in root.findall('.//parse'):
        tree_current = Tree.fromstring(parse.text)
        height = tree_current.height()
        for height_current in range(height):
            for subtree in tree_current.subtrees(\
                    lambda tree_current: tree_current.height() == height_current):
                if "NP" == subtree.label(): np_list.append(str(subtree)) 
    return np_list

if __name__ == '__main__':
    file_parsed = 'nlp.txt.xml'
    tree = ET.parse(file_parsed)
    np_list = s_expression_analysis(tree)
    print("\n".join(np_list))
