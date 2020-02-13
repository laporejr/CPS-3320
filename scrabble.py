#Robert Lapore Jr
#February 12th 2020
#CPS-3320 Python Programming

#This function takes the leter and gives you the score.

letter = input("Please enter a letter:")

def letterScore(letter):
	if letter in 'aeinorstul':
		return 1
	elif letter in 'dg':
		return 2

	elif letter in 'bcpm':
		return 3

	elif letter in 'fhvwy':
		return 4

	elif letter in 'k':
		return 5

	elif letter in 'jx':
		return 8

	elif letter in 'qz':
		return 10

	else:
		return 0

print(letterScore(letter.lower())) #convert any uppercase letters to lower



# This function takes takes the user's input word and provides the total score.

word = input("Please enter a word: ")
def wordScore(word):
	total= 0
	for i in range(len(word)):
		total = total + letterScore(word[i])

	return total

print(wordScore(word.lower()))  #convert any uppercase letters to lower

#program finished