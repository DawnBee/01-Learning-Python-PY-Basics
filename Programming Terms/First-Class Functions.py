# UNDERSTANDING FIRST-CLASS FUNCTIONS

'''
FIRST-CLASS FUNCTIONS:
- A programming language is said to have first-class functions if it treats functions as first-class citizens.
FIRST-CLASS CITIZEN:
- A first-class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the operations generally
availlable to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.
'''

# Note: If a function accepts other functions as arguments and return functions as a result of
# other functions its called 'Higher Order Function' (HOF).

def square(x):
	return x**2


f = square(5)

print(square) #When printing the function's name it displays its name and location at the file.
print(f) #When printing the variable where the function and its arguments are assigned, it returns the operation.


# SETTING OUR VARIABLE EQUAL TO UNEXECUTED FUNCTION:

func = square #By removing the parenthesis, we specify that we don't want to execute the function yet.

print(func(5)) #Here we can treat the variable 'func' as the 'square' function.

#PASSED FUNCTIONS AS ARGUMENTS &. RETURN FUNCTIONS AS A RESULT OF OTHER FUNCTIONS:

#EXAMPLE 1:
def my_map(func,args_list):
	result = []
	for i in args_list:
		result.append(func(i)) #'square' function executed here.
	return result

squares = my_map(square,[1,2,3,4,5]) #To prevent it from executing, removed the parenthesis after the function square.
print(squares)


#EXAMPLE 2:
def cube(x):
	return x**3

def a_map(func,args_list):
	result = [func(i) for i in args_list]
	return result

cubes = a_map(cube,[1,2,3,4,5])
print(cubes)


#EXAMPLE 3: RETURNING FUNCTIONS AS RESULT OF OTHER FUNCTIONS.

def logger(msg):
	def log_message():
		print('Log:',msg)

	return log_message #Returns the inner function 'log-message' 'w/o  executing'

log_hi = logger('Hi!')
log_hi()

log_hello = logger('Hello!')
log_hello()


#PRACTICAL EXAMPLE

def html_tag(tag):

	def wrap_text(msg):
		print('<{0}> {1} </{0}>'.format(tag,msg))

	return wrap_text #'wrap_text' function is waiting to be executed.

print_h1 = html_tag('h1') #This is the initial 'tag' argument.
print_h1('This is a Header') 
print_h1('Another Header') #These variables executes the inner-function 'wrap-text', and remembered the initial 'tag' argument.


print_p = html_tag('p')
print_p('This is our intro')





