# DECORATOR IV

# CHAINING/STACKING DECORATORS:

'''
@my_logger 
@my_timer --------------------------> The lower decorator on stack gets executed first.
def display_info(name,age):
	...............

*Chaining decorators this way will result in an issue where
the original function 'display_info' will be replaced with the
inner function 'wrapper_function' as it returns the wrapper function when 
it is executed.
'''

#DECORATING ALL THE WRAPPER FUNCTIONS WITH THE 'wraps' DECORATOR:

from functools import wraps

def my_logger(original_function):
	import logging
	logging.basicConfig(filename='decorator_4.log',level=logging.CRITICAL)

	@wraps(original_function) #Decorating the wrapper function with 'wraps' and original_function as argument.
	def wrapper_function(*args,**kwargs):
		logging.critical('Logged the arguments {}'.format(args))
		return original_function(*args,**kwargs)
	return wrapper_function

'''
This method will fix the chaining issues previously.
'''

def my_timer(orig_func):
	import time as t

	@wraps(orig_func) #Decorator 'wraps'.
	def wrapper(*args,**kwargs):
		t1 = t.time()
		result =  orig_func(*args,**kwargs)
		t2 = t.time() - t1
		print('{} function ran in {} sec'.format(orig_func.__name__,t2))
	return wrapper

@my_logger
@my_timer
def display_info(name,age):
	import time 
	time.sleep(1)
	print('Name: {} Age: {}'.format(name,age))


display_info('Leonardo',45)

'''
This will now display the correct original_function name which is 'display_info', instead of 'wrapper'.
'''