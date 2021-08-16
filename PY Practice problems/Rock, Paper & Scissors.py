# ROCK, PAPER & SCISSORS

'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the 
players want to start a new game)

Remember the rules:

• Rock beats scissors
• Scissors beats paper
• Paper beats rock
'''

print('Choices: \n • Rock \n • Paper \n • Scissors'.format('Rock','Paper','Scissors'))

def start_game():
	plyr_1 = input('Enter Name for Player 1: ')
	plyr_1_choice = input('Player 1 Pick a choice: ')

	plyr_2 = input('Enter Name for Player 2: ')
	plyr_2_choice = input('Player 2 Pick a choice: ')

	if plyr_1_choice == 'Rock' and plyr_2_choice == 'Paper':
		print('Player 2 Wins!')

	elif plyr_1_choice == 'Rock' and plyr_2_choice == 'Scissors':
		print('Player 1 Wins!')

	elif plyr_1_choice == 'Paper' and plyr_2_choice == 'Scissors':
		print('Player 2 Wins!')

	elif plyr_2_choice == 'Rock' and plyr_1_choice == 'Paper':
		print('Player 1 Wins!')

	elif plyr_2_choice == 'Rock' and plyr_1_choice == 'Scissors':
		print('Player 2 Wins!')

	elif plyr_2_choice == 'Paper' and plyr_1_choice == 'Scissors':
		print('Player 1 Wins!')

	else:
		print('Draw')


start_game()

while True:
	ask_for_newgame = input('Do you want to start a new game? ')

	if ask_for_newgame == 'Yes':
		start_game()
	else:
		print('Thank you for playing! get lost!')
		break




