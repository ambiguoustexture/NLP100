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

### 91. アナロジーデータの準備
Preparation of analogy data<br/>
准备类比数据

[単語アナロジーの評価データ](https://word2vec.googlecode.com/svn/trunk/questions-words.txt)
をダウンロードせよ．
このデータ中で": "で始まる行はセクション名を表す．
例えば，
": capital-common-countries"という行は，
"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，
"family"というセクションに含まれる評価事例を
抜き出してファイルに保存せよ．<br/>
Download the [word analogy evaluation data](https://word2vec.googlecode.com/svn/trunk/questions-words.txt). 
Lines starting with ":" in this data represent section names. 
For example, 
the line ": capital-common-countries" marks the beginning 
of a section called "capital-common-countries". 
From the downloaded evaluation data, 
extract the evaluation examples included in the section "family" 
and save them to a file.<br/>
下载[单词类比评估数据](https://word2vec.googlecode.com/svn/trunk/questions-words.txt)。 
此数据中以":"开头的行表示节名称。 
例如，行": capital-common-countries"标记了
名为"capital-common-countries"的部分的开头。 
从下载的评估数据中，提取"family"部分中包含的评估示例，
并将其保存到文件中。

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

### 93. アナロジータスクの正解率の計算
Calculating the accuracy rate of analogy tasks<br/>
计算类比任务的准确率

92で作ったデータを用い，
各モデルのアナロジータスクの正解率を求めよ．<br/>
Using the data created in 92, find the accuracy rate of analogy tasks for each model.<br/>
使用在92中创建的数据，找到每个模型的类比任务的准确率。

### 94. WordSimilarity-353での類似度計算
Similarity calculation with WordSimilarity-353<br/>
使用WordSimilarity-353进行相似度计算

[The WordSimilarity-353 Test Collection](http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/)
の評価データを入力とし，
1列目と2列目の単語の類似度を計算し，
各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，
90で作成した単語ベクトルに対して適用せよ．<br/>
Create a program that takes the evaluation data 
of [The WordSimilarity-353 Test Collection](http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/) 
as input, 
calculates the similarity between words in the first and second columns, 
and adds a similarity value to the end of each line. 
Apply this program to the word vector 
created in 85 and the word vector created in 90.<br/>
创建一个程序，
将[The WordSimilarity-353 Test Collection](http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/)
作为输入，
计算第一列和第二列中单词之间的相似度，
并将相似度值添加到每行的末尾。 
将此程序应用于在85中创建的单词向量和在90中创建的单词向量。

### 95. WordSimilarity-353での評価
Evaluation by WordSimilarity-353<br/>
通过WordSimilarity-353进行的评估

94で作ったデータを用い，
各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．<br/>
Using the data created in step 94, 
calculate the Spearman correlation coefficient 
between the ranking of similarity output from each model 
and the ranking of human similarity determination.<br/>
使用在步骤94中创建的数据，
计算每个模型输出的相似度等级与人类相似度确定等级之间的Spearman相关系数。

### 96. 国名に関するベクトルの抽出
Extract vector about country name<br/>
提取有关国名的向量

word2vecの学習結果から，
国名に関するベクトルのみを抜き出せ．<br/>
Extract only vectors related to country names 
from the learning results of word2vec.<br/>
从word2vec的学习结果中仅提取与国家名称有关的向量。

### 97. k-meansクラスタリング
k-means clustering<br/>
k均值聚类
96の単語ベクトルに対して，
k-meansクラスタリングをクラスタ数k=5
として実行せよ．<br/>
Perform k-means clustering on word vectors in step 96 with k = 5 clusters.<br/>
对步骤96中的词向量执行k = 5 均值聚类。

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

### 99. t-SNEによる可視化
Visualization with t-SNE
使用t-SNE进行可视化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．<br/>
Visualize the vector space with t-SNE for word vectors in steps 96.<br/>
使用t-SNE可视化步骤96的单词向量的向量空间。
