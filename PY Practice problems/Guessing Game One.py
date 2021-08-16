# GUESSING GAME ONE

'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to 
guess the number, then tell them whether they guessed too low, too high, or exactly 
right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

def guess_game():
	rand_num = random.randint(1,9)
	guess = 0
	guess_count = 0
	while guess != rand_num and 'exit':
		guess = input('Enter Guess: ')
		guess_count += 1

		if guess == 'exit':
			print('Number of Guesses:',guess_count-1)
			print('Thanks For Playing!')
			break

		guess = int(guess)
		
		if guess < rand_num:
			print('too low')
		elif guess > rand_num:
			print('too high')
		else:
			print('You Won!')
			print('Number of Guesses:',guess_count)
			print('====================')
			guess_game()

guess_game()


'''
# SOLUTION 2:
guess_count = 0

while True:
	ask_usr = int(input('Enter Guess: '))
	guess_count += 1

	if ask_usr < rand_num:
		print('too low')
	elif ask_usr > rand_num:
		print('too high')
	else:
		print('You Won!')
		print('Number of Guesses:',guess_count)
		break
'''