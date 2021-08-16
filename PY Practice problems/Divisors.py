# DIVISORS

'''
Create a program that asks the user for a number and then prints out a 
list of all the divisors of that number. (If you don’t know what a divisor is, 
it is a number that divides evenly into another number. For example, 
13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

ask_usr = int(input('Enter Number: '))

new_list = [i for i in range(1,ask_usr+1) if ask_usr % i == 0]

print(new_list)


'''
# Other Solution:
for i in range(1,ask_usr+1):
	if ask_usr % i == 0:
		new_list.append(i)
'''



