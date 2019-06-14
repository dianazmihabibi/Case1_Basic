import re
from collections import Counter

word_list = []
file = 'sample_text.txt'

#Read file
Words = open(file, 'r').read()

#Removing delimiter and replace with space
for char in '\xe2\x80\x93-.,\n\"\'!':
	Words=Words.replace(char,' ')
Words = Words.lower()

#Split the words
word_list = Words.split()

#Find how much the words on the txt files
numWords = len(word_list)
print '1. Jumlah kata pada text adalah : ', numWords, 'kata\n'

#Count words using Counter module
count = Counter(word_list).most_common()

#Find how much a word would appear in text
print '2. Jumlah kemunculan tiap kata dari teks adalah :\n', count, '\n'

#Rearrange the position of key and value to value in front of key
d = {}
for word in word_list:
	d[word] = d.get(word, 0) + 1

word_freq=[]

for key, value in d.items():
	word_freq.append((value, key))

word_freq.sort(reverse=True)

#Find how much words would appear only once
once = []
for value, key in d.items():
	if key == 1:
		once.append((value, key))
print '3. Jumlah kata yang muncul satu kali adalah :\n', once, '\n'

#Find words that most appear
print '4. Kata yang paling banyak muncul adalah :\n', max(word_freq), '\n'

#Find words that less appear
print '5. Kata yang paling sedikit muncul adalah :\n', min(word_freq), '\n'







