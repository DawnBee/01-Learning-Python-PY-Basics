# PROPERTY DECORATORS: GETTERS,SETTERS AND DELETERS

'''
-> 'Property' decorator allows to access a method like an attribute.
-> The name of the setter,getter and deleter must be the name of the property.
-> By the time I was coding this, I was using the latest python interpreter,
so even though we don't add the setter,getters and deleters decorators, the interpreter 
perhaps supports this functionality now, as I was experienced.
'''

class Employee:
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	@property #Property Decorator
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	#Setter Decorator
	@fullname.setter
	def fullname(self,name):
		first,last = name.split(' ')
		self.first = first
		self.last = last

	#Deleter Decorator
	@fullname.deleter
	def fullname(self):
		self.first = 'Not Found'
		self.last = ''
		print ('Deleted!')

	def email(self):
		return '{}.{}@email.com'.format(self.first,self.last)

	
emp_1 = Employee('Dean','Winchester',6000)
emp_2 = Employee('Sam','Winchester',5000)
emp_3 = Employee('John','Winchester',3000)

print(emp_3.email())

print(emp_1.email())

# Setting object to a different string:
emp_3.first = 'Rufus'

print(emp_3.fullname)

emp_1.fullname = 'Carl Archer' 

print(emp_1.fullname) 

# Calling the deleter decorator we created above:
del emp_1.fullname
print(emp_1.fullname)

del emp_2.fullname
print(emp_2.fullname)
