# Author：ambiguoustexture
# Date:   2020-02-02

def cipher (sequence):
    """replace with lowercase (219 - ascii code)
    :param sequence:    given string
    :return:            encrypted string
    """
    sequence_list = []
    res = ''

    for i in range(len(sequence)):
        if sequence[i].islower():
            sequence_list.insert(i, chr(219 - ord(sequence[i])))
        else:
            sequence_list.insert(i, sequence[i])

    for i in range (len(sequence)):
        res += sequence_list[i]

    return res

if __name__ == "__main__":
    sequence = "I am not an NLPer."
    print(cipher(sequence))
