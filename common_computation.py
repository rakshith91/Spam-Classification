'''
this file inlcudes read data for both decision tree and naive bayes
and other common functions
'''
from collections import namedtuple
import os
import time

a = time.time()
def list_of_words(folder):
	folder1= folder+"/spam"
	folder2 = folder+"/notspam"
	files = os.listdir(folder1)
	word_list =[]
	for doc in files:
		f = open(folder1+'/'+doc ,'r')
		words = f.read().replace('\n',' ').strip().split(' ')
		f.close()
		for word in words:
			word_list.append(word)	
	files = os.listdir(folder2)
	for doc in files:
		f = open(folder2+'/'+doc ,'r')
		words = f.read().strip().split(' ')
		for word in words:
			word_list.append(str(word))
		f.close()
	return  list(set(word_list))

Doc = namedtuple('Doc', list_of_words("./train"))

print len(list_of_words("./train"))
print time.time()-a
