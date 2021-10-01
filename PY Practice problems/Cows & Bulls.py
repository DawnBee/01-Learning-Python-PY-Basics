# COWS AND BULLS
'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the 
user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly
in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they
have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the 
user makes throughout the game and tell the user at the end.
'''

import random

def cows_bulls(giv_digits):
	yield_nums = [random.randint(0,9) for digit in range(giv_digits)]
	# print(f"Correct Guess: {str(yield_nums)}")
	divider = ('==============================\n')

	counter = 0
	while True:
		counter += 1
		print('---> Guess #{} <---'.format((counter)))
		print('Please enter {}-digit numbers:'.format(giv_digits))
		
		try:
			usr_guess = [int(i) for i in str(input('> '))]

			if len(usr_guess) != giv_digits:
				raise Exception

			if usr_guess == yield_nums:
				print('You Won!')
				print('It took you {} guess/es'.format(counter))
				break

			else:
				cows = 0
				bulls = 0

				for x in range(0,giv_digits):
					if usr_guess[x] == yield_nums[x]:
						cows += 1
					elif usr_guess[x] in yield_nums:
						bulls += 1

				print(f"Cows: {cows} Bulls: {bulls}")
			print(divider)

		except Exception:
			print('Invalid Input')
			print(divider)


# num_length = int(input("Enter Number's Length: "))
cows_bulls(4)
