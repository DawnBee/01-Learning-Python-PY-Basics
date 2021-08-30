# DECORATOR II

# PASSING ANY NUMBER OF POSITIONAL & KEYWORD ARGUMENTS
# TO OUR WRAPPER FUNCTION:

def decorator_function(original_function):
	def wrapper_function(*args,**kwargs): #This will allow us to pass any number of keyword & positional arguments.
		print('Wrapper executed this before {}'.format(original_function.__name__))
		return original_function(*args,**kwargs) #You can of course name this whatever you want, 
	return	wrapper_function			 		 #but in convention programmers use 'args' & 'kwargs'
	

@decorator_function #Decorator Syntax
def display_info(name,age):
	print("Ran with arguments '({},{})' ".format(name,age))

display_info('John',25)

'''
Take Note:
* --> Positional Arguments
** --> Keyword Arguments
'''

# CLASSES AS DECORATORS:

class decorator_class(object):
	def __init__(self,original_function):
		self.original_function = original_function

#'__call__' method will mimic the functionality of our 'wrapper_function'.

	def __call__(self,*args,**kwargs): #Will behave like the previous 'wrapper_function'
		print('__call__ method executed this before {}'.format(self.original_function.__name__))
		return self.original_function(*args,**kwargs)

@decorator_class 
def display(name,age):
	print('Ran with arguments [{}:{}]'.format(name,age))

display('Avril',39)
