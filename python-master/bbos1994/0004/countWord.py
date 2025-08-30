#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

import re

def wordStatistics(path):
	wordDict = {}
	with open(path,'r') as file:
		for line in file:
			wordsSplitByPunc = re.findall(r'[a-z0-9]+',line.lower())
			for words in wordsSplitByPunc:
				wordList = words.strip().split() # split by space
				for _word in wordList:
					if _word in wordDict:
						wordCount = wordDict.get(_word)
						wordCount+=1
						wordDict[_word] = wordCount
					else:
						wordDict[_word] = 1
			# wordListPerLine = line.lower().replace(string.punctuation,'').strip().split(' ')
	return wordDict

if __name__ == '__main__':
	import os
	print(os.getcwd()+'/words.txt')
	wordDict = wordStatistics(os.getcwd()+'/word.txt')
	for k in wordDict:
		print('key is \'%s\',value is %s' % (k, wordDict[k]))