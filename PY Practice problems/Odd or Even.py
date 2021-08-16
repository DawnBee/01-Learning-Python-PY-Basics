# ODD OR EVEN 

'''
Ask the user for a number. Depending on whether the number is even or odd, print out
an appropriate message to the user.

Extras:
1. If the number is a multiple of 4, print out different message.

2. Ask the user for two numbers: one number to check (call it num) and one 
number to divide by (check). If check divides evenly into num, tell that
to the user. If not, print a different appropriate message.
'''
divider = "==============================="


while True:
	num = int(input('Enter Number to Check: '))
	check = int(input('Enter Number to Divide by: '))

	
	if num % 4 == 0:
		print('Multiple of 4')
		print('Divides Evenly by 4')

	elif num % 2 == 0:
		print('Even')

	else:
		print('Odd')

	if num % check == 0:
		print('{} divides evenly by {}'.format(num,check))

	print(divider)