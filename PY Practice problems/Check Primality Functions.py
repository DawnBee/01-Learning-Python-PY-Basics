# CHECK PRIMALITY FUNCTIONS 

'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity 
to practice using functions, described below.
'''

def check_prime():
	while True:
		ask_usr = int(input('Enter Number: '))

		for i in range(2,ask_usr):
			if ask_usr % i == 0:
				print('Composite')
				break
		else:
			print('Prime')


check_prime()