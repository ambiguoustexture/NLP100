# Author：ambiguoustexture
# Date: 2020-02-12

import MeCab

def parse(file, file_parsed):
    with open(file) as text, open(file_parsed, 'w') as text_parsed:
        mecab_tagger = MeCab.Tagger()
        text = text.read()
        mecab_parsed = mecab_agger.parse(text)
        text_parsed.write(mecab_parsed)

        return mecab_parsed

def morphology_map(file_parsed):
    file_parsed = file_parsed.lstrip('\n')
    lines = file_parsed.splitlines()
    res = []

    for line in lines:
        line_current = line.replace('\t',',').split(',')
        if line_current[0] == 'EOS':
            break
        else:
            dict = {
                    'Surface' :line_current[0],
                    'base'    :line_current[-3],
                    'pos'     :line_current[1],
                    'pos1'    :line_current[2]
                    }
            res.append(dict)
    return res

if __name__ == "__main__":
    file = "neko.txt"
    file_parsed = "neko.txt.mecab"
    text_parsed = parse(file, file_parsed)
    res = morphology_map(text_parsed)
    print(res)
