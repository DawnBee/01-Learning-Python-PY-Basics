# DECORATOR I

def decorator_function(original_function): #Takes a function as argument.
	def wrapper_function():
		return original_function() #Returns original_function and executes it.
	return wrapper_function #Inner function waiting to be executed.

def display():
	print('display function ran')

decorated_display = decorator_function(display)

decorated_display() #Executes the inner function 'wrapper_function'

def dec_func(orig_func):
	def wrapper_func():
		print('Wrapper executed this before "{}"'.format(orig_func.__name__)) #This print statement executes before function.
		return orig_func() #Executes the 'exhibit' function.
	return wrapper_func

def exhibit():
	print('exhibit function ran')

decorated_exhibit = dec_func(exhibit)

decorated_exhibit()

'''
@decorator_function --> This is how you normally see decorator in python.
def display():
	print('display function ran')

display = decorator_function(display) --> This is the same as the above decorator syntax.
'''

