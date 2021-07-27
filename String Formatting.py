# STRING FORMATTING (String Interpolation)

''' Things to Remember:
	{} -> place holders
	.format(var)
'''

# Dictionary

Actor = {"First Name":'Tom',"Last Name": 'Hanks'}

format_actor = '''I'am {} {}'''.format(Actor["First Name"],Actor["Last Name"])

print(format_actor)

print('''I'm {0} {1}, {0} soldier!'''.format('a','warrior'))

# Grabbing specific fields in Dictionary

format_actor_2 = 'His name is {0[First Name]} {0[Last Name]}, yes you heard it right! {0[Last Name]}!'.format(Actor)

print(format_actor_2)

# In List

Sing_list = ['Avril','Jessica']

format_list = 'The List contains: {0[0]} & {0[1]}'.format(Sing_list)

print(format_list)

# In OOP

class Person:
	def __init__(self,f_name,l_name,age):
		self.f_name = f_name
		self.l_name = l_name
		self.age = age

	def fullname(self):
		return '{} {}'.format(self.f_name,self.l_name)

p1 = Person("John","Doe",21)
p2 = Person("Jane","Doe",20)

statement = '''I am {0.f_name} {0.l_name}, and I'm anonymous!'''.format(p1)

print(statement)

print(p2.fullname())

# By Keyword Arguments

sentence = "My name is {name} and I am {age} years old".format(name='Avril',age=39)

print(sentence)

# By unpacking dictionary

info_dict = {"Name":'Jane',"Age":27}

format_dict = '''I'm {Name} and I am {Age} years old!'''.format(**info_dict)

print(format_dict)

# Format and print-out numbers
for i in range(1,11):
	sentence = 'The value is {}'.format(i)
	print(sentence)

# 4 digits padding
for i in range(11,21):
	sentence = 'value is {:04}'.format(i)
	print(sentence)

# Format to decimal places
for i in range(21,31):
	sentence = 'float is {:.3f}'.format(i)
	print(sentence)

pi = 3.14159265

phrase = 'Pi is equal to {:.3f}'.format(pi)

print(phrase)

# Format with Commas
byte_size = '1MB is equal to {:,}KB'.format(1024)

print(byte_size)

bank_balance = 10000000000

print('Your acc balance is ${:,.2f}'.format(bank_balance))

# Format and print-out dates
import datetime as dt

my_date = dt.datetime(2021,7,26,6,11,33)

date_statement = '{:%B %d, %Y}'.format(my_date)

print(date_statement)

date_format = 'The month is {0:%B}, the day is {0:%d}(Monday) and the year is {0:%Y}'.format(my_date)

print(date_format)

# Formatting dates using the method date.today()
from datetime import date

print('The current date is: {:%A - %B %d, %Y}'.format(date.today()))