## 第10章: ベクトル空間法 (II)
Vector space method 02
向量空间法 其二

第10章では，
前章に引き続き単語ベクトルの学習に取り組む．<br/>
In Chapter 10, we will continue to learn word vectors 
as in the previous chapter.<br/>
在第10章中，我们将像上一章一样继续学习单词向量。

### 90. word2vecによる学習
Learning with word2vec<br/>
用word2vec学习

81で作成したコーパスに対して[word2vec](https://code.google.com/p/word2vec/)を適用し，
単語ベクトルを学習せよ．
さらに，学習した単語ベクトルの形式を変換し，
86-89のプログラムを動かせ．<br/>
Apply [word2vec](https://code.google.com/p/word2vec/) to the corpus 
created in step 81 to learn word vectors. 
Then, convert the learned word vector format and run the program from 86-89.<br/>
将[word2vec](https://code.google.com/p/word2vec/)应用于在步骤81中创建的语料库以学习单词向量。 
然后，转换训练得到的词向量格式并运行86-89的程序。
```python
import pickle
import numpy as np
from scipy import io
from collections import OrderedDict
import word2vec

file_corpus_shaped    = '../../ch09-Vector-space-method-01/compound_words_process_result.txt'
file_word2vec         = './word2vec.txt'
file_matrix_w2v       = './matrix_w2v.mat'
file_t_index_dict_w2v = './t_index_dict_w2v'

word2vec.word2vec(train=file_corpus_shaped, output=file_word2vec, size=300, threads=4, binary=0)

with open(file_word2vec) as vectors:
    vector = vectors.readline().split(' ')
    dict_size = int(vector[0])
    matrix_w2v_size = int(vector[1])

    t_index_dict_w2v = OrderedDict()
    matrix_w2v = np.zeros([dict_size, matrix_w2v_size], dtype=np.float64)

    for index, vector in enumerate(vectors):
        vector = vector.strip().split(' ')
        t_index_dict_w2v[vector[0]]    = index
        matrix_w2v[index] = vector[1:]

io.savemat(file_matrix_w2v, {'matrix_w2v': matrix_w2v})

with open(file_t_index_dict_w2v, 'wb') as t_index:
    pickle.dump(t_index_dict_w2v, t_index)
```
#### 86. Display Word Vector
```zsh
>>> import pickle
>>> from scipy import io
>>> file_matrix = './matrix_w2v.mat'
>>> file_t_index_dict_w2v = './t_index_dict_w2v'
>>> with open(file_t_index_dict_w2v, 'rb') as t_index_dict_w2v:
...     t_index_dict_w2v = pickle.load(t_index_dict_w2v)
...
>>> matrix_w2v = io.loadmat(file_matrix)['matrix_w2v']
>>> print(matrix_w2v[t_index_dict_w2v['United_States']])
[ 6.516200e-02 -1.622160e-01 -1.575080e-01  1.431391e+00 -7.549880e-01
 -3.868160e-01  1.033983e+00 -1.062307e+00  1.286642e+00  6.472350e-01
  1.184242e+00  3.849100e-02  4.611260e-01 -8.580850e-01 -3.410800e-01
  1.821654e+00  7.313180e-01  7.164880e-01  1.616750e-01  1.663404e+00
 -1.829218e+00 -9.803150e-01  7.163130e-01 -3.251230e-01  4.536800e-01
 -1.019445e+00 -1.623600e-01  5.216300e-01  1.501753e+00  3.811180e-01
 -5.262100e-01  2.083870e-01 -1.104954e+00  1.427667e+00 -1.611539e+00
  1.247158e+00 -4.591630e-01  1.370260e+00 -2.664867e+00 -1.439240e-01
 -9.170480e-01  6.829740e-01  1.466309e+00 -2.241200e-01 -6.866560e-01
 -4.550620e-01  7.815700e-02  1.129287e+00  1.842180e-01  5.429630e-01
  2.936290e-01 -3.244550e-01 -1.199418e+00 -4.611450e-01  1.041243e+00
  7.093000e-02 -1.278476e+00 -6.294800e-02  2.477310e-01  4.093500e-01
 -7.581000e-02 -1.181211e+00  1.619599e+00  3.149690e-01  3.118260e-01
 -5.560900e-02 -3.502300e-02 -7.190180e-01 -8.045510e-01 -1.159927e+00
  2.811860e-01 -7.958740e-01 -6.135190e-01  6.396230e-01  1.050343e+00
  3.878160e-01 -9.553610e-01  7.851000e-03  5.451750e-01  4.225210e-01
 -1.215348e+00 -9.251990e-01 -5.038130e-01 -2.361460e-01 -9.788320e-01
  1.047619e+00  4.580000e-04  3.782860e-01 -2.934870e-01 -3.468430e-01
  1.325300e-02  9.016160e-01  6.062740e-01  6.916020e-01  4.092600e-01
 -3.254870e-01 -1.805546e+00  5.647240e-01  2.043700e-01 -5.985730e-01
  1.200676e+00  3.572200e-02  5.597110e-01 -3.727800e-01  1.928900e-02
 -7.738960e-01 -6.746620e-01  1.484393e+00 -1.415153e+00  8.738650e-01
  2.813150e-01  1.689307e+00 -2.579840e-01  1.070654e+00  1.522540e-01
 -8.760470e-01 -1.141933e+00 -2.094020e-01  2.330220e-01  5.661760e-01
 -3.470230e-01  1.160140e-01  8.594800e-01  6.430970e-01  1.228804e+00
  1.075407e+00 -6.225210e-01 -5.355590e-01  3.306340e-01  9.863550e-01
  4.312100e-02  3.531580e-01 -1.219960e-01  1.219032e+00 -5.401490e-01
 -1.109000e-03  3.800960e-01 -9.730000e-03 -5.396270e-01  5.947230e-01
  4.226360e-01  3.251780e-01 -4.887530e-01 -1.416744e+00 -9.760700e-02
  2.551690e-01 -1.640148e+00  3.449540e-01  1.125520e-01 -1.767134e+00
  2.405040e-01 -3.812660e-01  4.299270e-01 -7.523960e-01 -5.718820e-01
  6.812350e-01 -5.522110e-01 -7.139200e-02 -5.563720e-01  1.064803e+00
 -8.200100e-02 -3.570800e-02  3.699830e-01  6.763920e-01 -7.129200e-02
  1.330690e-01 -1.811590e-01  7.211540e-01  1.347729e+00  9.022740e-01
 -4.130460e-01  1.341491e+00  1.824860e-01  2.407440e-01  9.776000e-02
  1.428867e+00  1.188074e+00  7.117210e-01  6.293410e-01  1.703344e+00
 -7.146580e-01 -4.303160e-01  1.911530e-01  1.350454e+00  1.492910e-01
  1.009613e+00 -6.097200e-01  2.947880e-01 -9.335950e-01  1.385914e+00
  1.191330e-01  2.081000e-01  1.608160e-01 -3.733090e-01 -4.964150e-01
  8.171410e-01 -6.179540e-01 -7.688630e-01 -3.056800e-01 -1.103477e+00
 -1.396739e+00  5.742020e-01 -1.475190e-01  6.992040e-01  9.468150e-01
  1.393149e+00 -8.434430e-01  9.268200e-02 -9.937100e-01 -2.236810e-01
  5.392020e-01  9.231650e-01  3.991340e-01 -1.873919e+00  8.794140e-01
 -2.733280e-01 -6.271390e-01  8.118630e-01 -2.933430e-01 -5.080870e-01
  1.760460e-01  2.992000e-02  1.320674e+00  1.606430e-01 -2.582970e-01
  1.290650e-01 -9.832110e-01 -6.309250e-01 -9.950120e-01 -1.236790e-01
  4.179280e-01 -1.905640e-01  1.158500e-02  1.317674e+00 -2.638120e-01
  2.622200e-01  1.381418e+00 -2.890180e-01  5.668710e-01 -4.676180e-01
  7.905220e-01 -2.726200e-02  2.126298e+00  8.974300e-02 -4.617000e-03
  9.167270e-01  1.195273e+00 -4.118500e-01 -4.300570e-01  5.230920e-01
 -7.203560e-01  1.318271e+00  8.854940e-01 -1.212290e-01  1.164580e+00
  1.622550e-01  9.276700e-01  1.920429e+00 -1.438150e-01 -1.571001e+00
  7.311520e-01  5.414600e-02 -6.736500e-01  2.948680e-01 -1.367000e+00
 -2.948690e-01  2.054640e-01  8.896310e-01  3.119080e-01  6.768500e-02
 -1.115039e+00 -5.480170e-01  6.366290e-01 -5.625360e-01  2.437550e-01
 -1.415000e-03 -5.334370e-01 -7.643220e-01  2.913250e-01  4.048100e-02
  2.652360e-01 -4.347830e-01  1.482070e-01  6.330720e-01 -6.004430e-01
  6.382300e-02 -7.073310e-01 -5.805800e-02  6.344800e-01 -1.056905e+00
  3.703090e-01 -1.273649e+00  1.142431e+00 -9.498500e-02  5.275870e-01
 -7.764000e-02 -2.507800e-02 -1.103031e+00 -4.478670e-01  1.874890e-01]
```

#### 87. Word Similarity
```zsh
➜ python similarity_cosine_w2v.py
Cosine similarity between "United_States" and "U.S": 0.8561059157257551
```

#### 88. 10 Words with High Similarity
```zsh
➜ python words_similar_with_England_w2v.py
Wales        0.7596929231316542
Scotland     0.7518911647767746
Ireland      0.6504271768416108
Britain      0.6220189793793658
Spain        0.5849140376261426
London       0.5651026306146962
Somerset     0.5584706532770636
Liverpool    0.557171859672741
Italy        0.551671743075501
Germany      0.549992477244345
```

#### 89. Analogy with Additive Constructivity
```zsh
➜ python analogy_with_additive_constructivity_w2v.py
Spain          0.9031150145701693
Italy          0.8186195604455722
Egypt          0.793828470274145
Austria        0.7875461399724515
Denmark        0.7870249924087551
Greece         0.7858603550270377
Sweden         0.7673030744691769
Russia         0.7565702035753025
Belgium        0.7562149231981151
Portugal       0.7475578362950815
```

### 91. アナロジーデータの準備
Preparation of analogy data<br/>
准备类比数据

[単語アナロジーの評価データ](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/questions-words.txt)
をダウンロードせよ．
このデータ中で": "で始まる行はセクション名を表す．
例えば，
": capital-common-countries"という行は，
"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，
"family"というセクションに含まれる評価事例を
抜き出してファイルに保存せよ．<br/>
Download the [word analogy evaluation data](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/questions-words.txt). 
Lines starting with ":" in this data represent section names. 
For example, 
the line ": capital-common-countries" marks the beginning 
of a section called "capital-common-countries". 
From the downloaded evaluation data, 
extract the evaluation examples included in the section "family" 
and save them to a file.<br/>
下载[单词类比评估数据](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/questions-words.txt)。 
此数据中，以": "开头的行表示章节。 
例如，行": capital-common-countries"标记了
名为"capital-common-countries"的部分的开头。 
从下载的评估数据中，提取"family"部分中包含的评估示例，
并将其保存到文件中。
```python
file_analogy_data        = './questions-words.txt'
file_analogy_data_family = './questions-words_family.txt'

with open(file_analogy_data) as analogy_data, \
        open(file_analogy_data_family, 'w') as analogy_data_family:
    flag_target = False
    for line in analogy_data:
        if flag_target:
            if line.startswith(': '):
                break
            print(line.strip(), file=analogy_data_family)
        elif line.startswith(': family'):
            flag_target = True
```
```zsh
➜ python analogy_data_prepare.py; head questions-words_family.txt
boy girl brother sister
boy girl brothers sisters
boy girl dad mom
boy girl father mother
boy girl grandfather grandmother
boy girl grandpa grandma
boy girl grandson granddaughter
boy girl groom bride
boy girl he she
boy girl his her
```

### 92. アナロジーデータへの適用
Application to analogy data<br/>
应用类比数据

91で作成した評価データの各事例に対して，
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，
その類似度を求めよ．
求めた単語と類似度は，
各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，
90で作成した単語ベクトルに対して適用せよ．<br/>
For each case in the evaluation data created in 91, 
calculate 
vec(word in the second column) - vec(word in the first column) + vec(word in the third column), 
Find the word with the highest similarity to the vector and its similarity.
Add the word and similarity to the end of each case. 
Apply this program to the word vector created in 85 and the word vector created in 90.<br/>
对于步骤91中创建的评估数据中的每种情况，
计算vec(第二列中的单词) - vec(第一列中的单词) + vec(第三列中的单词)，
查找与向量相似度最高的单词。
在每种情况的末尾添加单词和相似性。
将此程序应用于在85中创建的单词向量和在90中创建的单词向量。
```python
import time
import pickle
from scipy import io
from similarity_cosine_w2v import sim_cos

def find_max_similarity(file_matrix, file_t_index_dict, file_analogy_data, file_result):
    # load matrix
    try:
        matrix = io.loadmat(file_matrix)['matrix_w2v']
    except:
        matrix = io.loadmat(file_matrix)['context_matrix_X_PC']
    # load t_index_dict
    with open(file_t_index_dict, 'rb') as t_index_dict:
        t_index_dict = pickle.load(t_index_dict)
        keys = list(t_index_dict.keys())
    # find each max_similarity
    with open(file_analogy_data) as analogy_data, \
            open(file_result, 'wt') as result:
        for line in analogy_data:
            cols = line.split(' ')
            try:
                vec_additive = matrix[t_index_dict[cols[1]]] \
	                         - matrix[t_index_dict[cols[0]]] \
	                         + matrix[t_index_dict[cols[2]]]
                max_similarity, max_index, max_result = -1, 0, ''
                for index in range(len(t_index_dict)):
                    similarity = sim_cos(vec_additive, matrix[index])
                    if similarity > max_similarity:
                        max_index = index
                        max_similarity = similarity
                        max_result = keys[max_index]
            except KeyError:
                max_similarity = -1
                max_result     = ''
            print('{} {} {}'.format(line.strip(), max_result, max_similarity), file=result)

if __name__ == '__main__':
    file_matrix_w2v          = '../stuffs_90/matrix_w2v.mat'
    file_matrix_PC           = '../../ch09-Vector-space-method-01/context_matrix_X_PC'
    file_t_index_dict_w2v    = '../stuffs_90/t_index_dict_w2v'
    file_t_index_dict_PC     = '../../ch09-Vector-space-method-01/t_index_dict'
    file_analogy_data        = '../stuffs_91/questions-words_family.txt'
    file_result_by_w2v       = './result_w2v.txt'
    file_result_by_PC        = './result_PC.txt'

    time_start = time.time()
    find_max_similarity(file_matrix_w2v, file_t_index_dict_w2v, file_analogy_data, file_result_by_w2v)
    time_end   = time.time()
    print('With matrix from 90, cost', time_end - time_start, 's.')
    
    time_start = time.time()
    find_max_similarity(file_matrix_PC,  file_t_index_dict_PC, file_analogy_data, file_result_by_PC)
    time_end   = time.time()
    print('With matrix from 85, cost', time_end - time_start, 's.')
```
word2vec is better than contect co-occurence matrix on time.
```zsh
➜ python analogy_data_apply.py
With matrix from 90, cost 581.1286180019379 s.
With matrix from 85, cost 2759.7831168174744 s.
```

### 93. アナロジータスクの正解率の計算
Calculating the accuracy rate of analogy tasks<br/>
计算类比任务的准确率

92で作ったデータを用い，
各モデルのアナロジータスクの正解率を求めよ．<br/>
Using the data created in 92, find the accuracy rate of analogy tasks for each model.<br/>
使用在92中创建的数据，找到每个模型的类比任务的准确率。
```python
file_result_w2v = './stuffs_92/result_w2v.txt'
file_result_PC  = './stuffs_92/result_PC.txt'

with open(file_result_w2v) as result_w2v:
    count, total = 0, 0
    for line in result_w2v:
        cols = line.split(' ')
        total += 1
        if cols[3] == cols[4]:
            count += 1
    print('Accuracy of word2vec model:', count / total)

with open(file_result_PC)  as result_PC:
    count, total = 0, 0
    for line in result_PC:
        cols = line.split(' ')
        total += 1
        if cols[3] == cols[4]:
            count += 1
    print('Accuracy of PCA model:', count / total)
```
word2vec is better than contect co-occurence matrix on accuracy.
```zsh
➜ python accuracy_of_analogy_tasks.py
Accuracy of word2vec model: 0.09090909090909091
Accuracy of PCA model: 0.019762845849802372
```

### 94. WordSimilarity-353での類似度計算
Similarity calculation with WordSimilarity-353<br/>
使用WordSimilarity-353进行相似度计算

[The WordSimilarity-353 Test Collection](http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.zip)
の評価データを入力とし，
1列目と2列目の単語の類似度を計算し，
各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，
90で作成した単語ベクトルに対して適用せよ．<br/>
Create a program that takes the evaluation data 
of [The WordSimilarity-353 Test Collection](http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.zip)
as input, 
calculates the similarity between words in the first and second columns, 
and adds a similarity value to the end of each line. 
Apply this program to the word vector 
created in 85 and the word vector created in 90.<br/>
创建一个程序，
将[The WordSimilarity-353 Test Collection](http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.zip)
作为输入，
计算第一列和第二列中单词之间的相似度，
并将相似度值添加到每行的末尾。 
将此程序应用于在85中创建的单词向量和在90中创建的单词向量。
```python
import pickle
from scipy import io

from similarity_cosine import sim_cos

def similarity_bt_cols(file_t_index_dict, file_matrix, file_analogy_data, file_result):
    with open(file_t_index_dict, 'rb') as t_index_dict:
        t_index_dict = pickle.load(t_index_dict)

    try:
        matrix = io.loadmat(file_matrix)['matrix_w2v']
    except:
        matrix = io.loadmat(file_matrix)['context_matrix_X_PC']

    with open(file_analogy_data) as analogy_data, \
            open(file_result, 'wt') as result:
        flag_header = True
        for line in analogy_data:
            if flag_header:
                flag_header = False
                continue
            cols = line.split('\t')
            try:
                similarity = sim_cos(matrix[t_index_dict[cols[0]]],
                        matrix[t_index_dict[cols[1]]])
            except KeyError:
                similarity = -1
            print('{}\t{}'.format(line.strip(), similarity), file=result)

if __name__ == '__main__':
    file_matrix_w2v       = '../stuffs_90/matrix_w2v'
    file_matrix_PC        = '../../ch09-Vector-space-method-01/context_matrix_X_PC'
    file_t_index_dict_w2v = '../stuffs_90/t_index_dict_w2v'
    file_t_index_dict_PC  = '../../ch09-Vector-space-method-01/t_index_dict'
    file_analogy_data     = './wordsim353/combined.tab'
    file_result_w2v       = './result_w2v.tab'
    file_result_PC        = './result_PC.tab'

    similarity_bt_cols(file_t_index_dict_w2v, file_matrix_w2v, file_analogy_data, file_result_w2v)

    similarity_bt_cols(file_t_index_dict_PC,  file_matrix_PC,  file_analogy_data, file_result_PC)
```
```zsh
➜ head result_PC.tab result_w2v.tab
==> result_PC.tab <==
love	sex	6.77	0.25782348177344616
tiger	cat	7.35	0.4117488504172867
tiger	tiger	10.00	1.0
book	paper	7.46	0.35945468558612115
computer	keyboard	7.62	0.13132779889836232
computer	internet	7.58	0.24656645292291984
plane	car	5.77	0.3805249078670078
train	car	6.31	0.2710147356718218
telephone	communication	7.50	0.11368421841669417
television	radio	6.77	0.8109778838923809

==> result_w2v.tab <==
love	sex	6.77	0.547478873397767
tiger	cat	7.35	0.7964807866045261
tiger	tiger	10.00	0.9999999999999998
book	paper	7.46	0.530107734480692
computer	keyboard	7.62	0.6525765825029786
computer	internet	7.58	0.6669298018484214
plane	car	5.77	0.5516992613290509
train	car	6.31	0.5956607804285214
telephone	communication	7.50	0.5763507709928744
television	radio	6.77	0.7873306257208726
```

### 95. WordSimilarity-353での評価
Evaluation by WordSimilarity-353<br/>
通过WordSimilarity-353进行的评估

94で作ったデータを用い，
各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．<br/>
Using the data created in 94,
calculate the Spearman correlation coefficient between the rankings of models and human similarity judgments.
使用94中创建的数据，
对于每个模型，
计算模型相似度和人类相似度判断之间的Spearman相关系数。

Spearman's rank correlation coefficient:
![fomula_spearman_coe](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/stuffs_95/Spearman'sRankCorrelationCoefficient.svg)

```python
import numpy as np

def evaluate(file_result):
    with open(file_result) as result:
        human_judgements = []
        model_judgements = []
        N = 0
        for line in result:
            cols = line.split('\t')
            human_judgements.append(float(cols[2]))
            model_judgements.append(float(cols[3]))
            N += 1

    human_judgements_sorted = np.argsort(human_judgements)
    model_judgements_sorted = np.argsort(model_judgements)

    human_judgements_order = [0] * N
    model_judgements_order = [0] * N

    for i in range(N):
        human_judgements_order[human_judgements_sorted[i]] = i
        model_judgements_order[model_judgements_sorted[i]] = i

    # calculate the Spearman's rank correlation coefficient
    sum = 0
    for i in range(N):
        sum += pow(human_judgements_order[i] - model_judgements_order[i], 2)
    spearman_coefficient = 1 - (6 * sum) / (N * (pow(N, 2) - 1))
    return spearman_coefficient

if __name__ == '__main__':
    file_result_w2v = './stuffs_94/result_w2v.tab'
    file_result_PC  = './stuffs_94/result_PC.tab'
    print('Spearman\'s rank correlation coefficient by word2vec:', evaluate(file_result_w2v))
    print('Spearman\'s rank correlation coefficient by context co-occurrence matrix:',
            evaluate(file_result_PC))
```
```zsh
➜ python evaluation_by_wordsim353.py
Spearman's rank correlation coefficient by word2vec: 0.5161997429036609
Spearman's rank correlation coefficient by context co-occurrence matrix: 0.22625569082091868
```

### 96. 国名に関するベクトルの抽出
Extract vector about country name<br/>
提取有关国名的向量

word2vecの学習結果から，
国名に関するベクトルのみを抜き出せ．<br/>
Extract only vectors related to country names 
from the learning results of word2vec.<br/>
从word2vec的学习结果中仅提取与国家名称有关的向量。
```python
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

file_t_index_dict = './stuffs_90/t_index_dict_w2v'
file_matrix       = './stuffs_90/matrix_w2v'
file_countries    = '../ch09-Vector-space-method-01/countries.txt'

file_t_index_dict_countries = './t_index_dict_countries'
file_matrix_countries       = './matrix_countries'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

matrix = io.loadmat(file_matrix)['matrix_w2v']

t_index_dict_countries = OrderedDict()
matrix_countries = np.empty([0, 300], dtype=np.float64)
count = 0

with open(file_countries) as countries:
    for country in countries:
        try:
            country = country.strip().replace(' ', '_')
            index = t_index_dict[country]
            matrix_countries = np.vstack([matrix_countries, matrix[index]])
            t_index_dict_countries[country] = [count]
            count += 1
        except:
            pass

io.savemat(file_matrix_countries, {'matrix_countries':matrix_countries})
with open(file_t_index_dict_countries, 'wb') as t_index:
    pickle.dump(t_index_dict_countries, t_index)
```

### 97. k-meansクラスタリング
k-means clustering<br/>
k均值聚类
96の単語ベクトルに対して，
k-meansクラスタリングをクラスタ数k=5
として実行せよ．<br/>
Perform k-means clustering on word vectors in step 96 with k = 5 clusters.<br/>
对步骤96中的词向量执行k = 5 均值聚类。
```python
# Author: ambiguoustexture
# Date: 2020-03-11

import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
from sklearn.cluster import KMeans

file_t_index_dict = './stuffs_96/t_index_dict_countries'
file_matrix       = './stuffs_96/matrix_countries'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

matrix = io.loadmat(file_matrix)['matrix_countries']

predictions = KMeans(n_clusters=5).fit_predict(matrix)

result = zip(t_index_dict.keys(), predictions)

for country, group in sorted(result, key=lambda x: x[1]):
    print('{}\t{}'.format(group, country))
```
```zsh
➜ python countries_clusters.py > countries_clusters.txt; tail countries_clusters.txt
1	Ireland
1	Ukraine
1	Spain
1	Hungary
1	Romania
2	United_States
3	India
4	Japan
4	Canada
4	New_Zealand
```

### 98. Ward法によるクラスタリング
Clustering by Ward method
Ward法聚类

96の単語ベクトルに対して，
Ward法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．<br/>
Perform hierarchical clustering using the Ward method on word vectors in steps 96. 
Visualize the clustering result as a dendrogram.<br/>
使用Ward方法对步骤96的词向量执行分层聚类。 
将聚类结果可视化为树状图。
```python
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

file_t_index_dict = './stuffs_96/t_index_dict_countries'
file_matrix       = './stuffs_96/matrix_countries'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

matrix = io.loadmat(file_matrix)['matrix_countries']

ward = ward(matrix)

dendrogram(ward, labels=list(t_index_dict.keys()), leaf_font_size=8, orientation='left')
plt.show()
```
![countries_clusters_by_ward](https://github.com/ambiguoustexture/NLP-100-Knocks/blob/master/ch10-Vector-space-method-02/stuffs_98/countries_clusters_by_ward.png)
### 99. t-SNEによる可視化
Visualization with t-SNE
使用t-SNE进行可视化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．<br/>
Visualize the vector space with t-SNE for word vectors in steps 96.<br/>
使用t-SNE可视化步骤96的单词向量的向量空间。
