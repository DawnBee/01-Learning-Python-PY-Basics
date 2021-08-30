# UNDERSTANDING CLOSURES

'''
Closure - is a record storing a function together with an environment: a mapping associating
each free variable of the function with the value on storage location to which the name was bound 
when the closure was created. A closure, unlike a plain function, allows the function to access those
captured variable through the closure's reference to them, even when the function is invoked 
outside their scope.
'''

# Example 1:

def outer_func():
	message = 'Hi'
	def inner_func():
		print(message) #'message' is our "Free Variable" here.
	return inner_func()

outer_func()

# Example 2:

def outer():
	message = 'Hi'
	def innner():
		print(message)
	return innner

my_func = outer()

print(my_func)
print(my_func.__name__)

# Example 3:

def main(msg):
	message = msg 
	def inside():
		print(message)
	return inside

hello_func = main('Hello')
hello_func() #CLOSURE

hi_func = main('Hi')
hi_func() #CLOSURE

# Practical Example of Closure:

import os
import logging

os.chdir("C:/Users/John/OneDrive/Documents/My Files/Python - Projects/PY Scripts/Programming Terms")
print(os.getcwd())

logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
	def log_func(*args):
		logging.info('Running the "{}" function with the arguments {}'.format(func.__name__,args))
		print(func(*args))
	return log_func

def add(x,y):
	return x+y 

def sub(x,y):
	return x-y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)
