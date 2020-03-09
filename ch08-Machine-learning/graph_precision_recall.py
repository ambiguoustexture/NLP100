# Author: ambiguoustexture
# Date: 2020-03-09

import numpy as np
import matplotlib.pyplot as plt
from accuracy_measure import score

file_result = './k_fold_cross_validate_result.txt'
file_result_score = './precision_recall_result.txt'
res = []
with open(file_result) as result:
    for sentence in result:
        cols = sentence.split('\t')
        if len(cols) < 3:
            continue
        label = cols[0]
        if cols[1] == '-1':
            predict = 1.0 - float(cols[2])
        else:
            predict = float(cols[2])
        res.append((label, predict))

threshold_list = []
accuracy_list  = []
precision_list = []
recall_list    = []
f1_list        = []

for threshold in np.arange(0.02, 1.0, 0.02):
    with open(file_result_score, 'w') as result_score:
        for label, predict in res:
            if predict > threshold:
                result_score.write('{}\t{}\t{}\n'.\
                        format(label, '+1', predict))
            else:
                result_score.write('{}\t{}\t{}\n'.\
                        format(label, '-1', 1 - predict))

    accuracy, precision, recall, f1 = score(file_result_score)
    threshold_list.append(threshold)
    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)

plt.plot(threshold_list, accuracy_list, color='red', linestyle='dashdot', label='accuracy')
plt.plot(threshold_list, precision_list, color='green', linewidth=3, label='precision')
plt.plot(threshold_list, recall_list, color='blue', linewidth=3, label='recall')
plt.plot(threshold_list, f1_list, color='grey', linestyle='--', label='f1')
plt.title('Precision / Recall with Threshold')
plt.xlabel('Logistic Regression Model Classification Threshold')
plt.ylabel('Accuracy')
plt.legend(loc='lower left')
plt.show()
