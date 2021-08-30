# DECORATOR III

# PRACTICAL EXAMPLES:

#Example 1:
'''
This is basically the same as the previous decorator function, 
but now this will log arguments to the log file we specify for each execution. 
'''
def my_logger(original_function):
	import logging
	logging.basicConfig(filename='decorator_3.log',level=logging.INFO)
	def wrapper_function(*args,**kwargs):
		logging.info('Logged the arguments {}'.format(args,kwargs))
		return original_function(*args,**kwargs)
	return wrapper_function

@my_logger
def display_info(name,age):
	print("'display_info' ran with arguments [{}:{}]".format(name,age))
'''
Now we can re-use the 'my-logger' decorator anytime we want to add its
logging functionality to any new function.
'''
display_info('Avril',93)
display_info('Lavigne',39)


#Example 2:
'''
This will time how long the function runs.
'''
def my_timer(orig_func):
	import time as t 
	def wrapper(*args,**kwargs):
		t1 = t.time() #Captures the current time before the function's execution.
		result = orig_func(*args,**kwargs)
		t2 = t.time() - t1 #Captures the current time after the function's execution 
							#and subtract the initial time 't1'.
		print('{} function ran in: {:.3f} sec'.format(orig_func.__name__,t2))
	return wrapper

import time #Imported the 'time' module globally.

@my_timer #Timer Decorator
def display(first,last):
	time.sleep(3) #Delays time for atleast 3 seconds, to illustrate the 'my_timer' decorator.
	print('This rans with the arguments: {} {}'.format(first,last))


display('Avril','Lavigne')
display('Tom','Hanks')

