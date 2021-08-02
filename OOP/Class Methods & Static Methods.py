# CLASS METHODS AND STATIC METHODS

'''
Regular Methods = Automatically takes instance as the first argument,
which is 'self'.

Class Methods = Automatically takes the class as first argument, which is 'cls'.

Static Methods = Don't pass anything automatically, behaves like regular functions.
'''
import datetime

class Employee:
	raise_amount = 1.04 

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) 

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	# Class Method Example:
	# Takes the class instead of the instance. Must use 'cls'
	# because the word class had different meaning inside the language.
	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount

	# Using Class Methods as alternative constructor:
	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('+')
		return cls(first,last,pay)

	# Static Method Example:
	# Checks if given day is Saturday or Sunday.
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Employee('Dean','Winchester',6000)
emp_2 = Employee('Sam','Winchester',5000)
emp_3 = Employee('John','Winchester',3000)

emp_str_1 = "Bob+Singer+8000"
emp_str_2 = "Carl+Green+8500"
emp_str_3 = "Rufus+Black+10000"

#first,last,pay = emp_str_2.split('+')
#emp_4 = Employee(first,last,pay)

emp_4 = Employee.from_string(emp_str_1)

print(emp_4.fullname())

# Calling the class method to set a new value for the class variable:
Employee.set_raise_amt(2.06)

print(emp_3.raise_amount)

# Will also work on instances (NOT RECOMMENDED): 
emp_1.set_raise_amt(4.08)

print(emp_1.raise_amount)

my_date = datetime.date(2021,8,1)
print(Employee.is_workday(my_date))

from datetime import date as dt

curr_date = dt.today()

print(Employee.is_workday(curr_date))