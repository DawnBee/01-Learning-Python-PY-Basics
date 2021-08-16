# CHARACTER INPUT

'''
Create a program that asks the user to enter their name and their age. Print out 
a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out 
that many copies of the previous message. 
2. Print out that many copies of the previous message on separate lines.
'''

while True:
	from datetime import date as dt

	divider = "====================================="

	ask_name = input("Enter your name: ")
	ask_age = int(input("Enter your age: "))
	raw_calc = 100 - ask_age
	curr_date = dt.today()
	form_date = '{:%Y}'.format(curr_date)
	result = int(form_date) + raw_calc

	print("You will reach 100 in the year: {}!".format(result))

	print(divider)


