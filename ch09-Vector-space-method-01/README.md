## 第9章: ベクトル空間法 (I)
Vector space method 01<br/>
向量空间法 其一

[enwiki-20150112-400-r10-105752.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2)は，
2015年1月12日時点の英語のWikipedia記事のうち，
約400語以上で構成される記事の中から，
ランダムに1/10サンプリングした105,752記事のテキストをbzip2形式で圧縮したものである．
このテキストをコーパスとして，単語の意味を表すベクトル（分散表現）を学習したい．
第9章の前半では，コーパスから作成した単語文脈共起行列に主成分分析を適用し，
単語ベクトルを学習する過程を，いくつかの処理に分けて実装する．
第9章の後半では，学習で得られた単語ベクトル（300次元）を用い，
単語の類似度計算やアナロジー（類推）を行う．<br/>
[enwiki-20150112-400-r10-105752.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2) 
is a random sample of 1/10 of the English-language Wikipedia articles as of January 12, 2015, 
which consist of more than 400 words. 
This is the text of 105,752 articles compressed in bzip2 format. 
Using this text as a corpus, 
train a vector (distributed expression) that represents the meaning of a word. 
In the first half of Chapter 9, 
the process of learning word vectors 
by applying principal component analysis to the word context co-occurrence matrix 
created from the corpus is implemented in several processes. 
In the second half of Chapter 9, 
word similarity calculation and analogy (analog) are performed using word vectors (300 dimensions) 
obtained by learning.<br/>
[enwiki-20150112-400-r10-105752.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2)
是截至2015年1月12日的英语Wikipedia文章中的1/10个样本的随机样本，
文章包含约400或更多个单词。
一共105,752条以bzip2格式压缩的文章的文本。
使用这些文本作为语料库，训练一个代表单词含义的向量（分布式表达式）。
在第9章的前半部分，
通过几个步骤，
将主成分分析应用于从语料库生成的单词上下文共现矩阵来训练词向量。
在第9章的后半部分，
使用训练获得的词向量（300维）进行词相似度计算和类比。

なお，問題83を素直に実装すると，大量（約7GB）の主記憶が必要になる. 
メモリが不足する場合は，処理を工夫するか，
1/100サンプリングのコーパス
[enwiki-20150112-400-r100-10576.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r100-10576.txt.bz2)を用いよ．<br/>
If problem 83 is implemented straightforwardly, 
a large amount (about 7GB) of main memory will be required. 
If the memory is insufficient, 
devise the processing or use the corpus [enwiki-20150112-400-r100-10576.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r100-10576.txt.bz2) 
with 1/100 sampling.<br/>
如果直接开展步骤83，会用到大量（大约7GB）的内存。
如果内存不足，请先进行处理或使用1/100采样的语料库
[enwiki-20150112-400-r100-10576.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r100-10576.txt.bz2)。

### 80. コーパスの整形
Corpus shaping<br/>
语料库整形

文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである． 
ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう． 
そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，
各トークンに以下の処理を施し，単語から記号を除去せよ．
<br/>
The simplest way to convert a sentence into a sequence of words is to break it into words with space.
However, with this method, marks such as periods and parentheses 
at the end of the sentence are included in the word. 
So, after dividing the text of each line of the corpus into a list of tokens with blank characters, 
perform the following processing on each token to remove marks from words.<br/>
将句子转换为词序列最简单的方法，是以空格将其切分为词。
但是，使用这种方法，会产生末尾带有句点和括号之类符号的词。
因此，在将语料库的每一行文本划分为标记列表之后，
对每个标记执行以下处理以便从单词中去除记号。

- トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"<br/>
Remove the following characters at the beginning and end of the token: .,!?;: () [] '"<br/>
删除词例开头和结尾的以下字符： .,!?;: () [] '"

- 空文字列となったトークンは削除<br/>
Empty tokens are deleted<br/>
空词例需被删除

以上の処理を適用した後，
トークンをスペースで連結してファイルに保存せよ．<br/>
After applying processing above, 
connect the tokens with spaces and save them to a file.<br/>
上述处理后，用空格连接词例并将其保存在文件中。
```python
file_original = './enwiki-20150112-400-r100-10576.txt'
file_shaped   = './enwiki-20150112-400-r100-10576_shaped.txt'

with open(file_original) as text_original, \
        open(file_shaped, 'wt') as text_shaped:
    for line in text_original:
        words = []
        for word in line.split(' '):
            word = word.strip().strip('.,!?;:()[]\'"')
            if word != '':
                words.append(word)
        print(*words, sep=' ', end='\n', file=text_shaped)
```
```txt
# enwiki-20150112-400-r100-10576_shaped.txt
Anarchism

Anarchism is a political philosophy that advocates stateless societies often defined as self-governed voluntary institutions but that several authors have defined as more specific institutions based on non-hierarchical free associations Anarchism holds the state to be undesirable unnecessary or harmful While anti-statism is central anarchism entails opposing authority or hierarchical organisation in the conduct of human relations including but not limited to the state system

```

### 81. 複合語からなる国名への対処
Dealing with compound word as country's name<br/>
处理复合词组成的国家名称

英語では，複数の語の連接が意味を成すことがある．
例えば，アメリカ合衆国は"United States"，
イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，
指し示している概念・実体が曖昧である．
そこで，コーパス中に含まれる複合語を認識し，
複合語を1語として扱うことで，複合語の意味を推定したい．
しかしながら，
複合語を正確に認定するのは大変むずかしいので，
ここでは複合語からなる国名を認定したい．<br/>
In English, concatenation of multiple words can make sense. 
For example, the America is represented as "United States" 
and the Britain as "United Kingdom", 
but the words "United", "States", and "Kingdom" alone are ambiguous. 
Therefore, we want to estimate the meaning of a compound word 
by recognizing the compound word contained in the corpus 
and treating the compound word as one word. 
However, it is very difficult to accurately recognize compound words, 
so here we want to recognize country names consisting of compound words.<br/>
在英语中，串联起来的多个单词可以是有意义的。
例如，美国被表示为“United States”，英国被表示为“United Kingdom”，
但是仅仅作为单词的“United”，“States”和“Kingdom”是含混的。
因此，我们希望通过识别语料库中包含的复合词
并将复合词视为一个词来估计复合词的含义。
但是，复合词很难被准确识别，
因此这里我们仅识别由复合词组成的国家/地区名称。

インターネット上から国名リストを各自で入手し，
80のコーパス中に出現する複合語の国名に関して，
スペースをアンダーバーに置換せよ．
例えば，"United States"は"United_States"，
"Isle of Man"は"Isle_of_Man"になるはずである．<br/>
Obtain a list of country names on the Internet 
and replace spaces with underscores in compound words that appear in the corpus of step 80. 
For example, "United States" should be "United_States" 
and "Isle of Man" should be "Isle_of_Man".<br/>
获取互联网上的国家/地区名称列表，
对出现在步骤80得到的语料库中的复合词，用下划线替换空格。
例如，"United States"为"United_States"，"Isle of Man"为"Isle_of_Man"。
```python
file_shaped    = './enwiki-20150112-400-r100-10576_shaped.txt'
file_countries = './countries.txt'
file_compound_words = './compound_words_process_result.txt'

countries_set  = set()
countries_dict = {}
with open(file_countries) as countries:
    for country in countries:
        words = country.split(' ')
        if len(words) > 1:
            countries_set.add(country.strip())
            if words[0] in countries_dict:
                compound_len = countries_dict[words[0]]
                if not len(words) in compound_len:
                    compound_len.append(len(words))
                    compound_len.sort(reverse=True)
            else:
                countries_dict[words[0]] = [len(words)]

with open(file_shaped) as text_shaped, \
        open(file_compound_words, 'w') as compound_words:
    for line in text_shaped:
        words = line.strip().split(' ')
        res = []
        flag_skip = 0
        for i in range(len(words)):
            if flag_skip > 0:
                flag_skip -= 1
                continue
            if words[i] in countries_dict:
                flag_hit = False
                for length in countries_dict[words[i]]:
                    if ' '.join(words[i:i + length]) in countries_set:
                        res.append('_'.join(words[i:i+length]))
                        flag_skip = length - 1
                        flag_hit = True
                        break
                if flag_hit:
                    continue
            res.append(words[i])
        print(*res, sep=' ', end='\n', file=compound_words)
```
```zsh
➜ wc -l compound_words_process_result.txt
  284434 compound_words_process_result.txt
➜ grep "United_" -o compound_words_process_result.txt | wc -l
    6311
```

### 82. 文脈の抽出
Context extraction<br/>
上下文提取

81で作成したコーパス中に出現するすべての単語tに関して，
単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
ただし，文脈語の定義は次の通りとする．<br/>
Write out all pairs of word t and context word c in tab-delimited format 
for all words t appearing in the corpus created in 81. 
The definition of the context word is as follows.<br/>
以制表符分隔的格式
对81中的语料库中出现的所有单词 t 写出所有单词对 t 和上下文单词 c。 
上下文词的定义如下。

- ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）<br/>
Extract d words before and after the word t as context word c 
(however, the context word does not include the word t itself)<br/>
提取单词t之前和之后的d个单词作为上下文单词c（但是，上下文单词不包括单词t本身）

- 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．<br/>
Each time a word t is selected,
the context width d is randomly determined within the range of {1,2,3,4,5}.<br/>
每次选择单词t时，上下文宽度d在{1,2,3,4,5}范围内随机确定。
```python
import random

file_compound_words = './compound_words_process_result.txt'
file_context        = './context.txt'

with open(file_compound_words) as compound_words, \
        open(file_context, 'w') as context:
    for index, line in enumerate(compound_words):
        words = line.strip().split(' ')
        for j in range(len(words)):
            t = words[j]
            d = random.randint(1, 5)
            for k in range(max(j - d, 0), min(j + d + 1, len(words))):
                if j != k:
                    print('{}\t{}'.format(t, words[k]), file=context)
```
```
➜ head context.txt
Anarchism	is
Anarchism	a
Anarchism	political
is	Anarchism
is	a
is	political
a	Anarchism
a	is
a	political
a	philosophy
```

### 83. 単語／文脈の頻度の計測
Measuring word / context frequency<br/>
测量 词/上下文 频率

82の出力を利用し，以下の出現分布，および定数を求めよ．<br/>
Using the output of 82, find the following distribution and constants.<br/>
使用82的输出，找到以下分布和常数。

- f(t,c) : 単語tと文脈語cの共起回数<br/>
Number of co-occurrences of word t and context words c<br/>
单词t和上下文单词c的共现次数

- f(t,∗) : 単語tの出現回数<br/>
Number of occurrences of word t<br/>
单词t的出现次数

- f(∗,c) : 文脈語cの出現回数<br/>
Number of occurrences of context words c<br/>
上下文词c的出现次数

- N : 単語と文脈語のペアの総出現回数<br/>
Total number of occurrences of word-context word pairs<br/>
词-上下文词 对的出现总数
```python
from collections import Counter
import pickle

file_context    = './context.txt'
file_counter_tc = './tc_counter'
file_counter_t  = './t_counter'
file_counter_c  = './c_counter'

tc_counter = Counter()
t_counter  = Counter()
c_counter  = Counter()

tc_current, t_current, c_current = [], [], []

with open(file_context) as context:
    for index, line in enumerate(context, start=1):
        line = line.strip()
        words = line.split('\t')
        tc_current.append(line)
        t_current.append(words[0])
        c_current.append(words[1])
        if index % 1000000 == 0:
           tc_counter.update(tc_current)
           t_counter.update(t_current)
           c_counter.update(c_current)
           tc_current, t_current, c_current = [], [], []

tc_counter.update(tc_current)
t_counter.update(t_current)
c_counter.update(c_current)

with open(file_counter_tc,  'wb') as tc:
    pickle.dump(tc_counter, tc)
with open(file_counter_t,   'wb') as t:
    pickle.dump(t_counter,  t)
with open(file_counter_c,   'wb') as c:
    pickle.dump(c_counter,  c)```
```
N:
```
➜ wc -l context.txt
 68031796 context.txt
```
### 84. 単語文脈行列の作成
Create word context matrix<br/>
创建单词上下文矩阵

83の出力を利用し，単語文脈行列Xを作成せよ．
ただし，行列Xの各要素Xtcは次のように定義する．<br/>
Create a word context matrix X using the output of 83. 
Where each element Xtc of the matrix X is defined as follows.<br/>
使用83的输出创建单词上下文矩阵X。
矩阵X的每个元素Xtc定义如下。

- f(t,c)≥10ならば，Xtc = PPMI(t,c) = max{log(N×f(t,c))/(f(t,∗)×f(∗,c)),0}
if f(t,c)≥10: Xtc = PPMI(t,c) = max{log(N×f(t,c))/(f(t,∗)×f(∗,c)),0}

- f(t,c)<10ならば，Xtc = 0
else: Xtc = 0

ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
なお，行列Xの行数・列数は数百万オーダとなり，
行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
<br/>
Here, PPMI (t, c) is a statistic called Positive Pointwise Mutual Information. 
Note that the number of rows and columns of matrix X is on the order of several millions, 
and it is impossible to put all the elements of the matrix in main memory. 
Fortunately, most elements of matrix X are zero, so you only need to write out the nonzero elements.<br/>
在这里，PPMI(t，c)是一个统计量，称为正 点间互信息。 
请注意，矩阵X的行和列数约为数百万，
并且不可能将矩阵的所有元素都放在主存储器上。
所幸，矩阵X的大多数元素为零，因此您只需要写出非零元素。

```python
import math
import pickle
from collections import Counter
from collections import OrderedDict
from scipy import sparse, io

file_tc_counter       = './tc_counter'
file_t_counter        = './t_counter'
file_c_counter        = './c_counter'
file_context_matrix_X = './context_matrix_X'
file_t_index_dict     = './t_index_dict'

N = 68031841
with open(file_tc_counter, 'rb') as tc:
    tc_counter = pickle.load(tc)
with open(file_t_counter,  'rb') as t:
    t_counter  = pickle.load(t)
with open(file_c_counter,  'rb') as c:
    c_counter  = pickle.load(c)

t_index_dict = OrderedDict((key, i) for i, key in enumerate(t_counter.keys()))
c_index_dict = OrderedDict((key, i) for i, key in enumerate(c_counter.keys()))

t_size, c_size = len(t_index_dict), len(c_index_dict)
context_matrix_X = sparse.lil_matrix((t_size, c_size))

for tc, f_tc in tc_counter.items():
    if f_tc > 10:
        words = tc.split('\t')
        t, c = words[0], words[1]
        ppmi = max(math.log((N * f_tc) / (t_counter[t] * c_counter[c])), 0)
        context_matrix_X[t_index_dict[t], c_index_dict[c]] = ppmi

# save context_matrix_X as Matlab file
io.savemat(file_context_matrix_X, {'context_matrix_X': context_matrix_X})

with open(file_t_index_dict, 'wb') as t_index:
    pickle.dump(t_index_dict, t_index)
```

### 85. 主成分分析による次元圧縮
Dimensional compression by principal component analysis<br/>
通过主成分分析进行尺寸压缩

84で得られた単語文脈行列に対して，主成分分析を適用し，
単語の意味ベクトルを300次元に圧縮せよ．<br/>
Apply principal component analysis to the word context matrix obtained in step 84, 
and compress the meaning vector of the word to 300 dimensions.
将主成分分析应用于在步骤84中获得的单词上下文矩阵，
并将单词语义向量压缩到300维。
```python
>>> from scipy import sparse, io
>>> file_context_matrix_X = './context_matrix_X'
>>> context_matrix_X = io.loadmat(file_context_matrix_X)['context_matrix_X']
>>> context_matrix_X.shape
(388668, 388599)
>>> import sklearn.decomposition
>>> context_matrix_X_PC = sklearn.decomposition.TruncatedSVD(300).fit_transform(context_matrix_X)
>>> context_matrix_X_PC.shape
(388668, 300)
```

### 86. 単語ベクトルの表示
Display word vector<br/>
显示单词向量

85で得た単語の意味ベクトルを読み込み，
"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．<br/>
Read the meaning vector of the word obtained in step 85 and display the "United States" vector.
Note that "United States" is internally represented as "United_States".<br/>
读取在步骤85中获得的词向量，并显示词"United States"。 注意，"United States"在内部表示为"United_States"。
```python
>>> import pickle
>>> from scipy import io
>>> file_context_matrix_X_PC = './context_matrix_X_PC'
>>> file_t_index_dict = './t_index_dict'
>>> with open(file_t_index_dict, 'rb') as t_index_dict:
...     t_index_dict = pickle.load(t_index_dict)
...
>>> context_matrix_X_PC = io.loadmat(file_context_matrix_X_PC)['context_matrix_X_PC']
>>> print(context_matrix_X_PC[t_index_dict['United_States']])
[ 3.33600558e+00 -8.78380574e-01  1.10290167e-01  6.14253073e+00
  2.63084244e+00 -1.33378743e+00 -2.07975473e+00  9.46230402e-02
 -2.28001119e-01 -1.93131129e-01  1.18620360e+00  1.88003713e+00
 -1.64126007e+00 -2.69655059e+00 -1.83005678e+00  2.65592846e+00
  5.72013336e-02 -3.92560088e+00  8.83360863e-01  1.99726386e-01
 -5.72899277e-02  1.55160519e+00 -4.12413472e-02 -1.45772532e-01
  1.60485952e+00  6.82243596e-01  4.09560748e-01  2.42060699e+00
 -2.30810389e+00 -3.11965922e+00 -2.43281169e+00  6.71712235e-01
  6.97988457e-01  1.64079730e+00 -1.65291394e+00  1.11201819e+00
  2.58538099e+00  1.30549359e+00 -1.45254802e-01  8.89946960e-01
  4.66935546e-01  1.38906463e+00 -1.04314690e+00  1.78675115e+00
  4.30661459e-01 -1.70828083e-01  6.24509223e-01  3.41536560e-01
  8.74739416e-01 -1.45767848e+00  1.20334575e+00 -2.24908963e-01
  1.57778901e+00 -7.70038312e-03  6.24877338e-01  1.56845516e+00
  4.63921537e-01  3.73894371e-01  6.90685994e-01  2.83677425e-01
 -8.95085984e-01  2.60854427e+00 -1.41598932e+00  4.24277468e-02
 -6.48377375e-02 -1.15007947e-01 -8.47965792e-01  5.50527602e-01
  1.63491174e-01  2.00458177e+00 -4.96736556e-02  6.38732941e-01
  2.16299316e+00  1.78704310e+00  1.69243217e+00  5.33141849e-01
 -1.07861532e-01 -7.59279080e-01 -5.69676514e-01 -5.87676204e-01
 -9.05826840e-01 -2.04454277e+00  2.35209823e-03 -1.14362701e+00
 -1.32467074e-01 -8.68664844e-01  9.52526147e-01  3.78386195e-01
  9.85781497e-01 -6.20831177e-01 -1.44038677e+00 -1.53245025e+00
 -6.40640295e-01 -5.43140413e-01  1.87679752e-01  9.55865321e-01
 -7.71745467e-01 -6.79483038e-02 -8.70736630e-01 -1.09033480e-01
  1.82956687e+00 -1.18279139e+00 -4.27062144e-01 -3.38812905e-01
 -1.65979812e-02 -5.95057446e-01  1.70074803e+00 -8.50162892e-01
  1.72987053e-01  1.65749801e-01 -4.58461477e-01 -7.28587344e-02
  2.37763260e-01  1.18082485e+00  4.81952740e-01 -6.80832638e-02
 -6.78677696e-01 -7.48441236e-01 -2.97577297e-01 -8.88492798e-01
  3.19888261e-01 -4.79333666e-01 -1.28193894e+00 -2.51611325e+00
  8.13582618e-01  3.72543065e-01  6.54868251e-02  1.35128294e+00
 -2.11320402e-01  4.68456915e-01 -4.45195717e-02 -6.14505178e-01
  1.38046278e+00 -2.90918647e-01 -1.08423212e-01 -4.82039455e-01
  1.02959324e+00 -2.44287563e-01 -2.04210172e+00 -9.69545659e-02
  9.51536746e-02  9.39636528e-01  1.32106809e+00 -3.14319853e+00
  9.07977694e-01 -1.29583441e-01 -1.22899526e-01 -9.85273429e-01
  9.28775599e-01 -2.76058405e-01 -5.08424181e-01  2.28819598e-01
 -5.33261746e-01 -6.83505181e-01 -1.96042644e-01 -4.66173247e-04
 -7.69987862e-01  6.37152552e-01 -1.40666354e-01 -1.43840881e+00
  8.94753575e-01 -1.22352972e+00 -5.94170379e-01 -6.80620112e-01
 -1.86551458e+00  6.98668416e-01  6.19404457e-04  1.03267546e+00
  4.02322595e-01  3.44892919e-01 -2.05404039e-02  2.74299284e-01
  4.78518990e-01 -5.29114993e-02  7.90913673e-01  2.31926912e-02
 -9.68071067e-02 -1.26063428e+00 -4.08788450e-01 -4.84139543e-01
  1.56630578e+00  3.01595773e-01 -1.58435570e-01 -3.56765032e-01
  1.17443780e+00 -1.97108816e-01  2.33482039e-02 -7.67571723e-01
 -4.80882898e-01  1.05520702e+00  5.49336755e-01  2.10323471e-01
  2.48251014e-01 -2.36406694e+00 -3.98543941e-01 -6.96588221e-01
  9.84492899e-01 -9.38485435e-01  6.27119994e-01 -1.52400455e+00
 -5.88700651e-03 -1.01724981e+00 -1.35856769e+00 -2.08276310e-01
 -6.77496740e-01 -3.72832486e-01 -3.93372159e-01 -4.16050434e-01
  5.88233912e-01 -4.66526114e-01 -1.63477150e-01 -2.26327051e-01
 -1.25145389e-01 -9.53027474e-01 -9.41047252e-02 -6.33190572e-02
  1.39971261e+00 -2.06539732e+00 -4.41144688e-01  2.23048816e-02
  1.64423373e+00  3.67561271e-01  6.62879170e-01  1.82566122e-01
 -9.28273962e-01  7.96265930e-01  7.81420529e-01  4.32829205e-01
 -5.08459510e-01 -8.48990274e-02  2.46003481e-01 -6.64093472e-01
 -4.63199299e-01 -7.97812230e-01  1.25841701e+00 -8.26938654e-02
  8.75311443e-01  4.77638672e-01  6.86855734e-01 -8.78381595e-01
 -6.16212429e-02 -3.27673759e-01  5.13540594e-01  3.63748563e-01
 -2.12016108e-01  1.24609057e-01 -1.34226729e+00  2.00258755e-01
 -1.13542538e+00 -2.07563170e-01  7.65329807e-01  4.04041663e-01
  2.43382893e-01  3.78900025e-01  1.24087826e-02  4.25563604e-01
 -2.39378929e-01  1.69206899e-01  3.47532022e-01 -1.11235805e-01
  4.52660701e-01 -1.91298462e-01 -6.99634550e-01 -2.09633424e-01
  2.61488935e-01  3.33789347e-01 -1.37051600e+00 -4.57868231e-01
 -3.59495120e-01 -3.92163787e-01  1.07046720e-01  9.66405902e-01
  2.38250937e-01  1.50168566e-02 -1.82647699e-01  3.09556021e-01
  5.25283338e-01 -3.34102445e-01 -2.33017016e-01  1.20450044e+00
 -6.56958106e-01 -5.47122831e-02 -2.82011173e-01  7.03035544e-01
 -5.37906752e-02  3.31301929e-01  3.54665649e-01  8.15086652e-01
 -2.88154334e-01  6.32379698e-01  1.24715273e+00 -8.51942949e-01
 -6.49735329e-03  7.05039557e-01 -5.80681758e-01 -9.26964489e-01
  1.71541510e-01  6.51991916e-01 -4.71225563e-01 -3.78150650e-01]
```

### 87. 単語の類似度
Word similarity<br/>
单词相似度

85で得た単語の意味ベクトルを読み込み，
"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．<br/>
Read the semantic vector of the word obtained in step 85 and calculate the cosine similarity between "United States" and "U.S.". Note, however, that "U.S." is internally represented as "U.S."<br/>
读取在步骤85中获得的单词的词向量，并计算"United States"和"U.S."之间的余弦相似度。
但是请注意，"U.S."在内部表示为"U.S"。
```python
import pickle
import numpy as np
from scipy import io

def sim_cos(word_a, word_b):
    """
    calculate the cosine similarity
    """
    mul_ab = np.linalg.norm(word_a) * np.linalg.norm(word_b)
    if mul_ab == 0:
        return -1
    else:
        return np.dot(word_a, word_b) / mul_ab

if __name__ == '__main__':
    file_context_matrix_X_PC = './context_matrix_X_PC'
    file_t_index_dict        = './t_index_dict'

    with open(file_t_index_dict, 'rb') as t_index_dict:
        t_index_dict = pickle.load(t_index_dict)

    context_matrix_X_PC = io.loadmat(file_context_matrix_X_PC)['context_matrix_X_PC']
    word_a = context_matrix_X_PC[t_index_dict['United_States']]
    word_b = context_matrix_X_PC[t_index_dict['U.S']]

    print('Cosine similarity between "United_States" and "U.S":', sim_cos(word_a, word_b))
```
```zsh
➜ python similarity_United_States-US.py
Cosine similarity between "United_States" and "U.S": 0.8256988144545605
```

### 88. 類似度の高い単語10件
10 words with high similarity<br/>
高度相似的10个词

85で得た単語の意味ベクトルを読み込み，
"England"とコサイン類似度が高い10語と，その類似度を出力せよ．<br/>
Read the semantic vector of the word obtained in step 85, 
and output 10 words with high cosine similarity to "England" and their similarity<br/>
读取在步骤85中获得的单词的词向量，
并输出与“England”具有高余弦相似度的10个单词及其相似度
```python
import pickle
import numpy as np
from scipy import io
from similarity_cosine import sim_cos

file_context_matrix_X_PC = './context_matrix_X_PC'
file_t_index_dict        = './t_index_dict'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

context_matrix_X_PC = io.loadmat(file_context_matrix_X_PC)['context_matrix_X_PC']

word_England       = context_matrix_X_PC[t_index_dict['England']]
words_similarities = [sim_cos(word_England, context_matrix_X_PC[i])
        for i in range(len(t_index_dict))]
words_similarities_sorted = np.argsort(words_similarities)
words = list(t_index_dict.keys())

for index in words_similarities_sorted[-2:-12:-1]:
    print(words[index].ljust(12, ' '), words_similarities[index])
```
```zsh
➜ python words_similar_with_England.py
Scotland     0.616724731859635
Australia    0.5911118851962176
Wales        0.5624891979996978
France       0.5618514619134919
Japan        0.55865118835873
Germany      0.5419670503592768
Italy        0.5333627250283722
Ireland      0.5134767992278451
Spain        0.48963085196114614
Europe       0.4636289733997487
```

### 89. 加法構成性によるアナロジー
Analogy with additive constructivity<br/>
类比加法构造性

85で得た単語の意味ベクトルを読み込み，
vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．<br/>
Read the semantic vector of the word obtained in 85, 
calculate vec("Spain") - vec("Madrid") + vec("Athens"),
Output 10 words with high similarity to the vector and their similarity.<br/>
读取在85中获得的单词的向量，计算vec("Spain") - vec("Madrid") + vec("Athens")，
并输出10个与该向量最相似的词及其向量。
```python
import pickle
import numpy as np
from scipy import io
from similarity_cosine import sim_cos

file_context_matrix_X_PC = './context_matrix_X_PC'
file_t_index_dict        = './t_index_dict'

with open(file_t_index_dict, 'rb') as t_index_dict:
    t_index_dict = pickle.load(t_index_dict)

context_matrix_X_PC = io.loadmat(file_context_matrix_X_PC)['context_matrix_X_PC']

words_additive = context_matrix_X_PC[t_index_dict['Spain']] \
        - context_matrix_X_PC[t_index_dict['Madrid']] \
        + context_matrix_X_PC[t_index_dict['Athens']]
words_similarities = [sim_cos(words_additive, context_matrix_X_PC[i])
        for i in range(len(t_index_dict))]
words_similarities_sorted = np.argsort(words_similarities)
words = list(t_index_dict.keys())

for index in words_similarities_sorted[:-11:-1]:
    print(words[index].ljust(14, ' '), words_similarities[index])
```
```zsh
➜ python analogy_with_additive_constructivity.py
Spain          0.8907717290490869
Sweden         0.8875350479294913
Austria        0.8547812867707035
Denmark        0.8000015848337706
Italy          0.7918456833102121
Belgium        0.7814917768618459
Netherlands    0.7790052507477426
Germany        0.7708831723539175
Télévisions    0.7597184200052526
France         0.7436473060240459
```

