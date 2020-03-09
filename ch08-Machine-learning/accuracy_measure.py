# Author：ambiguoustexture
# Date: 2020-03-09

def score(file_result):
    """
    score using confusionmatrix
    """
    TP, FP, TN, FN = 0, 0, 0, 0
    with open(file_result) as result:
        for line in result:
            cols = line.split('\t')
            if len(cols) < 3:
                continue
            if   cols[0] == '+1':
                if cols[1] == '+1':
                    TP += 1
                else:
                    FN += 1
            else:
                if cols[1] == '+1':
                    FP += 1
                else:
                    TN += 1

    accuracy = (TP + TN) / (TP + FP + FN + TN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = (2 * recall * precision) / (recall + precision)
    return accuracy, precision, recall, f1

if __name__ == '__main__':
    file_result = './labeling_result.txt'
    accuracy, precision, recall, f1 = score(file_result)
    print('accuracy:'.ljust(14, ' '), accuracy)
    print('precision:'.ljust(14, ' '), precision)
    print('recall:'.ljust(14, ' '), recall)
    print('f1:'.ljust(14, ' '), f1)
