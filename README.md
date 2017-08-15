# Spam-Classification
Classifies if a mail is spam or not with 98% accuracy. 

Problem Statement:
------------------
This is a classic machine learning problem where we have to train a model for spam classification. We have used a simple
bag of words model where we represent every document in terms of just an unordered bag of words instead of taking
grammar/context into consideration.

Problem Formulation:
--------------------
Every document is represented as a list of feature values in a vector. And every value of the vector corresponds to a
unique word from the training set. We have considered two types of feature values:
1. Binary :- 
- Every value in the data point vector is either a 0 or 1 .
- 0 represents that the particular word didnt occur in the document.
- 1 represents that the particular word has occurred atleast once in that document.

2.Continous:- 
- Every value in the vector corresponds to a unique word in the training set.
- Every value is a number >=0 and it represents the number of times that particular word has occurred.
- So basically we are considering the count of word occurrences in a document as the feature type.

Algorithms implemented:
-----------------------
1. Naive Bayes:
===============
- In this algorithm we need to calculate the posterior probability of P(S=1/w1,w2 and so on) .
- To make things easier we take the likelihood ratio of P(S=1/w1,w2,w3 and so on)/P(S=0/w1,w2,w3 and so on). For this we need to calculate the likelihood and prior probabilities.

Assumptions made:- 
1. probability of occurrence of words is considered to be independent of each other.
2. Some stop words like 'the','to','from' etc are not considered into our classification as they are equally likely to occur in a spam or a non spam document.

Our program implementation:
---------------------------
1. Loading the data from the training files
2. Preprocessing the data and modifying the data into necessary format.
3. Calculate the Likelihood dictionaries : For both binary and continuous cases
4. Calculate the prior probabilities
5. Test on the test data using the model generated

Problems faced:
---------------
In some scenarios we could encounter a word in test data that has never occurred in the train data. So, that word would have a zero likelihood probability and thus making our product of likelihoods zero and thus making our posterior probability zero.
Our fix: We have assumed a very minimalistic probability for that kind of words. This is similar to laplace smoothing.

2. Decission Tree: 
=================

For the same problem we are building a decision tree using features as words and class label being 1 for spam and 0 for not spam. The whole training data has been converted into a tabular format where every row represents a document and every column represents a feature/word. We have taken both binary and continuous feature values just as like in the naive bayes  case.

Our program implementation:
---------------------------
1. Loading the data from the training files
2. Preprocessing the data and modifying the data into necessary format.
3. Build a decision tree:
- We have implemented a n-ary tree => A node can have multiple children depending on the number of distinct values a feature has.
- At every node the feature which gives the maximum Information gain is selected for splitting.
- The tree is built in a depth first manner .
- There are few stopping conditions for the tree :
a. When depth is exceeding maximum specified depth
b. At a node when the data is pure => either completely belonging to spam or completely belonging to not spam.

4. Test on the test data using the model generated

Results:-
--------
NaiveBayes:  When we use continuous feature values the accuracy is slightly higher than when we use binary feature values.In continuous case If a word is occurring more number of times it would be having higher likelihood probability than another word which occurs very less number of times. Whereas in  the binary case both would have same probability as we are only concerned if it occurs or not, and not about its frequency. This could be a good reason why the continuous case is giving
better results in Naive Bayes.

Decission Tree: Here binary feature values are giving slightly higher accuracy value than continuous feature values.
This could be because, in the continuous case as the breadth of the tree is also large along with the depth of the tree we are getting a very large tree and as we have only few thousand data points a lot of leaf nodes would be having very few data points.

