# SPECIAL MAGIC/DUNDER METHODS

'''
Ex:
__init__ <-- 'Dunder' (Double underscore)

# Common Special Methods
print(emp_1)
repr(emp_1)
str(emp_1)

__repr__ = meant to be an unambiguous representation of the object should
be use for (debugging and logging). Meant to be seen by developers.

__str__ = readable representation of an object, meant to be seen by users.
'str' will use 'repr' as a fallback, so it's good to have 'str' as a minimum.

'''

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

# Re-create same object using __repr__:
	def __repr__(self):
		return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
 
# This will now return the string that we specified on our special __repr__ method above, 
# instead of returning an unclear message.

# __str__ method example:
	def __str__(self):
		return '{} is an instance of the Employee class.'.format(self.fullname())

# __add__ method example:
# Customizes how addition works in our object.
	def __add__(self,other):
		return self.pay + other.pay

# __len__ method example:
	def __len__(self):
		return len(self.fullname())

emp_1 = Employee('Dean','Winchester',6000)
emp_2 = Employee('Sam','Winchester',5000)
emp_3 = Employee('John','Winchester',3000)

print(emp_3) # will now use the __str__ method as a minimum.
print(emp_2) 

# Access __repr__ and __str__ method specifically:
print(repr(emp_2))
print(str(emp_1))

# Background method executing each time we run the 'repr' & 'str' method we created.
print(emp_3.__repr__())
print(emp_2.__str__())

print(emp_2 + emp_3) # Uses the __add__ method we created above.

# Background execution sample:
print(int.__add__(1,2))
print(str.__add__('a','b'))

print(len(emp_3)) # Uses the __len__ method we created above.

