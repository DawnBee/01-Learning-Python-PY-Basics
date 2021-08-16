# STRING LISTS

'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

while True:
	ask_usr = input('Enter Word: ')

	if ask_usr[::-1] == ask_usr:
		print('Palindrome')
	else:
		print('Not Palindrome')

