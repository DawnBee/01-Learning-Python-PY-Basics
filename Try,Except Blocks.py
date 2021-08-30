# TRY/EXCEPT BLOCKS

#Try/Except blocks are use to display user-friendly errors.

'''
try:
except Exception:
else:
finally:
'''

#Using 'Try' accept blocks:
try:
	f = open('Hello-world.log')
except Exception:
	print('Sorry,wrong syntax')

try: 
	f = open('No_where.txt')
	print('Hello World')
except FileNotFoundError:
	print("File doesn't Exist")


#Naming error Exception blocks:
try:
	f = open('No_way_home.txt')
	print('817240')
except FileNotFoundError as e:
	print('Salut!',e)


#Using 'else' block:
import os 

os.chdir("C:/Users/John/OneDrive/Documents/My Files/Python - Projects/PY Scripts")

try:
	f = open('exception-test.txt') #Since the filename is correct it will not throw an exception error.
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read()) #And will execute the codes within the 'else' clause.
	f.close()


#Using 'finally' block:
try:
	f = open('exception-test.txt')
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()
finally: #'finally' block will execute codes no matter what happens.
	print('Executing Finally')

'''
#Raising Exception:
try:
	print('Hello-world')
	if 'Hello-world' != 'Hello':
		raise Exception #Calls the exception block if it hits the conditional given.
'''
