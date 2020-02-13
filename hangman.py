#Robert Lapore
#February 12th 2020
#CPS-3320 Python Programming

# Hangman game!
#This program answers questions 2,3,4 and 5.
# chooses one of the words to play by using random function
import random

rand = random.randint(0,2)
words = [['p', 'i', 'a','n', 'o'], ['v', 'o', 'i', 'c', 'e'], ['f','l','u','t','e']]


A = words[rand]
L = ['_', '_', '_', '_', '_']

incorrect = 0
play = True

while play == True:

	# Ask the user to guess a letter

	letter = str(input("Guess a letter: "))

	# Check to see if that letter is in the answer
	if letter in A:    
		i = 0
		for currentletter in A:

			# If the letter the user guessed is found in the answer,
			# set the underscore in the user's answer to that letter

			if letter == currentletter:

				L[i] = letter

			i = i + 1

		
		# Display what the player has thus far (L) with a space
		# separating each letter

		print(' '.join(str(n) for n in L))

		# Test to see if the word has been successfully completed,
		# and if so, end the loop

		if A == L:
			play = False
			print("Great Job!")

		#If letter is not in the game, tell the user it's wrong 
		#Allow the user only to guess wrong 6 times or otherwise the game is over
	else:
		print(' '.join(str(n) for n in L))
		print("BAD GUESS")
		incorrect+=1
		if incorrect==6:
			play = False
			print("GAME OVER")

#program finished.