#!/usr/bin/env python3
'''
1. Of the letters that appear in the dataset, what letter appears the least frequently?
2. What is the length of the word that appears the most in the dataset?
3. Which letter appears 17001 times?
4. How many words in total?
5. Which letter appears 7100 times?
6. Number of unique words in the dataset
7. The word that appears exactly 101 times in the dataset
'''

words = [
	['', 'one',	'two', 'three',	'four',	
	'five',	'six', 'seven',	'eight', 'nine'],

	['ten',	'eleven', 'twelve',	'thirteen',	'fourteen',
	'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'],

	['', '', 'twenty', 'thirty', 'fourty', 
	'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
]

def toWord(x : int) -> str:
	word = ('0' * 5 + str(x))[-5:]
	result = []

	if word[0] == '1':
		return 'ten thousand'

	if word[1] != '0':
		result.append(words[0][int(word[1])] + ' thousand')

	if word[2] != '0':
		result.append(words[0][int(word[2])] + ' hundred')

	if word[3] == '1':
		result.append(words[1][int(word[4])])

	else:
		if word[3] != '0':
			result.append(words[2][int(word[3])])
		if word[4] != '0':
			result.append(words[0][int(word[4])])
	return ' '.join(result)

data = [toWord(x) for x in range(1, 10001)]

letters = {}
for n in data:
	for c in n:
		if c in letters:
			letters[c] += 1
		else:
			letters[c] = 1
letters.pop(' ')
sortedLetters = (sorted(letters.items(), key=lambda x:x[1]))

words = {}
for w in (' '.join(data)).split(' '):
	if w in words:
		words[w] += 1
	else:
		words[w] = 1
sortedWords = (sorted(words.items(), key=lambda x:x[1]))

ans = [
	sortedLetters[0][0],
	len(sortedWords[-1][0]),
	[_[0] for _ in sortedLetters if _[1] == 17001][0],
	sum([_[1] for _ in sortedWords]),
	[_[0] for _ in sortedLetters if _[1] == 7100][0],
	len(sortedWords),
	[_[0] for _ in sortedWords if _[1] == 101][0]
]
print(''.join([str(_).upper() for _ in ans]))
print(f'''
1. {sortedLetters[0][0]}
2. {len(sortedWords[-1][0])}
3. {[_[0] for _ in sortedLetters if _[1] == 17001]}
4. {sum([_[1] for _ in sortedWords])}
5. {[_[0] for _ in sortedLetters if _[1] == 7100]}
6. {len(sortedWords)}
7. {[_[0] for _ in sortedWords if _[1] == 101]}
''')
print(sortedLetters, sortedWords)
