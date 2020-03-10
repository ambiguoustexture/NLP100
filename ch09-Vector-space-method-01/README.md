## 第9章: ベクトル空間法 (I)
Vector space method<br/>
向量空间法

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
在第9章的前半部分中，
通过将主成分分析应用于从语料库创建的单词上下文共现矩阵来训练单词向量的过程
分为几个步骤实现。
在第9章的后半部分，使用训练获得的单词向量（300维）执行单词相似度计算和类比（模拟）。

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
将句子转换为词序列最简单的方法是将其分解为带有空格的词。
但是，使用这种方法，会产生末尾附带句点和括号之类记号的词。
因此，在将语料库的每一行文本划分为带有空格字符的标记列表之后，
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
and replace spaces with underscores in compound words that appear in the 80 corpus. 
For example, "United States" should be "United_States" 
and "Isle of Man" should be "Isle_of_Man".<br/>
获取互联网上的国家/地区名称列表，
对出现在这80个语料库中的复合词，用下划线替换空格。
例如，"United States"为"United_States"，"Isle of Man"为"Isle_of_Man"。

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

- 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
Each time a word t is selected,
the context width d is randomly determined within the range of {1,2,3,4,5}.
每次选择单词t时，上下文宽度d在{1,2,3,4,5}范围内随机确定。

### 83. 単語／文脈の頻度の計測
Measuring word / context frequency<br/>
测量 词/上下文 频率

82の出力を利用し，以下の出現分布，および定数を求めよ．

- f(t,c) : 単語tと文脈語cの共起回数<br/>
Number of co-occurrences of word t and context words c
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

### 85. 主成分分析による次元圧縮
Dimensional compression by principal component analysis<br/>
通过主成分分析进行尺寸压缩

84で得られた単語文脈行列に対して，主成分分析を適用し，
単語の意味ベクトルを300次元に圧縮せよ．<br/>
Apply principal component analysis to the word context matrix obtained in step 84, 
and compress the meaning vector of the word to 300 dimensions.
将主成分分析应用于在步骤84中获得的单词上下文矩阵，
并将单词语义向量压缩到300维。

### 86. 単語ベクトルの表示
Display word vector<br/>
显示单词向量

85で得た単語の意味ベクトルを読み込み，
"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．<br/>
Read the meaning vector of the word obtained in step 85 and display the "United States" vector.
Note that "United States" is internally represented as "United_States".<br/>
读取在步骤85中获得的词向量，并显示词"United States"。 注意，"United States"在内部表示为"United_States"。

### 87. 単語の類似度
Word similarity<br/>
单词相似度

85で得た単語の意味ベクトルを読み込み，
"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．<br/>
Read the semantic vector of the word obtained in step 85 and calculate the cosine similarity between "United States" and "U.S.". Note, however, that "U.S." is internally represented as "U.S."<br/>
读取在步骤85中获得的单词的词向量，并计算"United States"和"U.S."之间的余弦相似度。
但是请注意，"U.S."在内部表示为"U.S"。

### 88. 類似度の高い単語10件
10 words with high similarity<br/>
高度相似的10个词

85で得た単語の意味ベクトルを読み込み，
"England"とコサイン類似度が高い10語と，その類似度を出力せよ．<br/>
Read the semantic vector of the word obtained in step 85, 
and output 10 words with high cosine similarity to "England" and their similarity<br/>
读取在步骤85中获得的单词的词向量，
并输出与“England”具有高余弦相似度的10个单词及其相似度

### 89. 加法構成性によるアナロジー
Analogy with additive constructivity<br/>
类比与加法构造性

85で得た単語の意味ベクトルを読み込み，
vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．<br/>
Read the semantic vector of the word obtained in 85, 
calculate vec("Spain") - vec("Madrid") + vec("Athens"),
Output 10 words with high similarity to the vector and their similarity.<br/>
读取在85中获得的单词的向量，计算vec("Spain") - vec("Madrid") + vec("Athens")，
并输出10个与该向量最相似的词及其向量。
