import logging
import os

os.chdir("C:/Users/John/OneDrive/Documents/My Files/Python - Projects/PY Scripts/Logging Basic")
print(os.getcwd())

'''
NOTE: logging configs will not work when run at the same time. 'basicConfig' configures
the root logger in a certain file, which means 2 scripts that are sharing the same log 
file will not be possible, unless done by using modular logging(Logging Advance).
'''
# LOGGING LEVELS
'''
10-DEBUG: Detailed information, typically of interest only when diagnosing problems.

20-INFO: Confirmation that things are working as expected.

30-WARNING(Default): An indication that something unexpected happened, or indicative of some 
problem in the near future (e.g. 'disk space low'). The software is still working as expected.

40-ERROR: Due to more serious problems, the software has not able to perform some functions.

50-CRITICAL: A Serious error, indicating that the program itself maybe unable to continue running.
'''

num_1 = 5
num_2 = 3

def add(x,y):
	return x + y

def mult(x,y):
	return x * y

add_result = add(num_1,num_2)

mult_result = mult(num_1,num_2)


# Replacing 'print' statements with 'log' statements:

print('Add: {} + {} = {}'.format(num_1,num_2,add_result))

print('Multiply: {} * {} = {}'.format(num_1,num_2,mult_result))

logging.debug('Add: {} + {} = {}'.format(num_1,num_2,add_result))

logging.info('Multiply: {} * {} = {}'.format(num_1,num_2,mult_result))

# Changing Logging levels using 'basicCongif':

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

logging.info('Multiply: {} * {} = {}'.format(num_1,num_2,mult_result))

logging.debug('Add: {} + {} = {}'.format(num_1,num_2,add_result))

# Logging to log files instead of the console:
logging.basicConfig(filename='basic_logging.log',level=logging.INFO)
logging.basicConfig(filename='basic_logging.log',level=logging.DEBUG)

# Changing 'format' in log file:
logging.basicConfig(filename='basic_logging.log',level=logging.ERROR,format='%(asctime)s:%(levelname)s:%(message)s')
logging.basicConfig(filename='basic_logging.log',level=logging.CRITICAL,format='%(levelname)s:%(asctime)s:%(message)s')

logging.error('Multiply: {} * {} = {}'.format(num_1,num_2,mult_result))
logging.critical('Add: {} + {} = {}'.format(num_1,num_2,add_result))

# Adding logging to OOP:
logging.basicConfig(filename='employee_log.log',level=logging.INFO,format='%(message)s:%(levelname)s:%(asctime)s')

logging.basicConfig(filename='employee_log.log',level=logging.CRITICAL,format='%(levelname)s:%(message)s:%(asctime)s')

class Employee:
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

		logging.info('Added the object: {}'.format(self.fullname))
		logging.critical('Created the instance email: {}'.format(self.email()))

	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def email(self):
		return '{}.{}@email.com'.format(self.first,self.last)

pers_1 = Employee('Bob','Dylan',5000)
pers_2 = Employee('Peter','Osbern',6000)
pers_3 = Employee('George','Smith',2000)


