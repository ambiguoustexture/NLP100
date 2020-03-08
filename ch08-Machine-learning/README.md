## 第8章: 機械学習
本章では，Bo Pang氏とLillian Lee氏が公開している
[Movie Review Dat](http://www.cs.cornell.edu/people/pabo/movie-review-data/)の
[sentence polarity dataset v1.0](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt)を用い，
文を肯定的（ポジティブ）もしくは否定的（ネガティブ）に分類するタスク（極性分析）に取り組む．<br/>
In this chapter, using the 
[sentence polarity dataset v1.0](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt) of the 
[Movie Review Dat](http://www.cs.cornell.edu/people/pabo/movie-review-data/) published by Bo Pang and Lillian Lee, 
work on the described task (polarity analysis) of classifying sentences as positive (positive) or negative (negative).<br/>
在本章中，使用Bo Pang和Lillian Lee发行的 
[Movie Review Dat](http://www.cs.cornell.edu/people/pabo/movie-review-data/) 的 
[sentence polarity dataset v1.0](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt)，
尽力完成将句子分类为正（positive）或负（negative）的任务（极性分析）。


### 70. データの入手・整形
Obtaining and shaping data<br/>
获取和整理数据

[文に関する極性分析の正解データ](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz)
を用い，
以下の要領で正解データ（sentiment.txt）を作成せよ．<br/>
Create correct answer data (sentiment.txt) using the 
[correct answer data from the polarity analysis for the sentence](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz) as follows.<br/>
使用如下[句子极性分析中的正确答案数据](http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz)创建正确答案数据（sentiment.txt）。

- rt-polarity.posの各行の先頭に"+1 "という文字列を追加する
（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）<br/>
Add the string "+1" to the beginning of each line in rt-polarity.pos 
(polarity label "+1" followed by a space, followed by the positive sentence)<br>
将字符串“ +1”添加到rt-polarity.pos中每行的开头
（极性标签“ +1”，后跟一个空格，后跟肯定句的内容）
- rt-polarity.negの各行の先頭に"-1 "という文字列を追加する
（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）<br/>
Add a string "-1" to the beginning of each line of rt-polarity.neg
(Polarity label "-1" followed by a space, followed by the contents of the negative sentence.)<br/>
将字符串“ -1”添加到rt-polarity.neg中每行的开头
（极性标签“ -1”，后跟一个空格，后跟否定句的内容）

- 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，
正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．<br/>
Concatenate the contents of 1 and 2 above, 
and create a sentiment.txt that randomly rearranges the lines. 
Check the number of positive examples (positive sentences) and the number of negative examples (negative sentences).<br/>
结合上面1和2的内容，并创建一个sendiment.txt来随机重新排列各行，
检查肯定示例（肯定句）和否定示例（否定句）的数量。

### 71. ストップワード
Stop word<br/>
停用词

英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
それ以外は偽を返す関数を実装せよ．
さらに，その関数に対するテストを記述せよ．<br/>
Create a list of English stop words (stop list). 
Furthermore, implement a function that returns true if the word (character string) given in the argument is included in the stoplist, 
and returns false otherwise. Write a test for the function.<br/>
创建英语停用词列表。
此外，实现一个函数，如果参数中给定的单词（字符串）包含在非索引词表中，则返回true，否则返回false。
为该功能编写一个测试。<br/>

### 72. 素性抽出
Feature extraction<br/>
特征提取

極性分析に有用そうな素性を各自で設計し，
学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．<br/>
Design features that are likely to be useful for polarity analysis, 
and extract features from training data. 
The minimum baseline for the feature would be to remove the stopwords from the review and to stem each word.<br/>
设计可能对极性分析有用的特征，并从训练数据中提取特征。
该功能的最低基准是从评论中删除停用词并阻止每个词。

### 73. 学習
Learning<br/>
学习

72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．<br/>
Train a logistic regression model using the features extracted in 72.
使用72中提取的特征训练逻辑回归模型。

### 74. 予測
Predict<br/>
预测

73で学習したロジスティック回帰モデルを用い，
与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．<br/>
Using the logistic regression model learned in step 73, 
implement a program to calculate the polarity label of the given sentence ("+1" for positive examples, "-1" for negative examples) and its predicted probability.
使用在步骤73中训练的逻辑回归模型，
实现一个程序来计算给定句子的极性标签（对于肯定示例，“ + 1”，对于否定示例，“-1”）及其预测概率。

### 75. 素性の重み
Feature weight<br/>
特征权重

73で学習したロジスティック回帰モデルの中で，
重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
In the logistic regression model learned in 73, 
check the top 10 features with high weight and the top 10 features with low weight.
在73训练的逻辑回归模型中，
检查权重较高的前10个特征和权重较低的前10个特征。

### 76. ラベル付け
Labeling<br/>
标注

学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．<br/>
Apply a logistic regression model to the training data and output the correct labels, 
predicted labels, and predicted probabilities in tab-delimited format.<br/>
将逻辑回归模型应用于训练数据，并以制表符分隔的格式输出正确的标签，预测的标签和预测正确的概率。

### 77. 正解率の計測
Measurement of accuracy rate<br/>
准确率的测量

76の出力を受け取り，
予測の正解率，正例に関する適合率，再現率，
F1スコアを求めるプログラムを作成せよ．<br/>
Write a program that receives the output of 76 and calculates the correct answer rate of the prediction, 
the precision rate for the correct example, the recall rate, and the F1 score.
编写一个程序，接收76的输出，并计算预测的正确答案率，正确示例的正确率，召回率和F1分数。

### 78. 5分割交差検定
5-fold cross validation<br/>
5-fold交叉验证

76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，
モデルの汎化性能を測定していない．
そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．<br/>
在76-77的实验中，用于学习的案例也用于评估，因此不能说这是有效的评估。
换句话说，分类器评估记忆训练样本的性能，而不衡量模型的泛化性能。
因此，使用5-fold交叉验证来计算极性分类的正确答案率，准确率，召回率和F1分数。

### 79. 適合率-再現率グラフの描画
Drawing precision / recall graph<br/>
绘制准确率/召回率图

ロジスティック回帰モデルの分類の閾値を変化させることで，
適合率-再現率グラフを描画せよ．<br/>
Draw a precision-recall graph by changing the classification threshold of the logistic regression model.<br/>
通过更改逻辑回归模型的分类阈值绘制精确召回图。
