import logging

#logging.basicConfig(filename='employee.log',level=logging.INFO,format='%(levelname)s:%(name)s:%(message)s')

#Creating Loggers:
logger = logging.getLogger(__name__)

#Specify a Log file using file handler:
file_handler = logging.FileHandler('employee.log')

#Adding the file handler to our logger:
logger.addHandler(file_handler)

#Setting logging level to our logger variable:
logger.setLevel(logging.INFO)

#Create a Formatter:
formatter = logging.Formatter('[%(levelname)s]>[%(name)s]>[%(message)s]')

#Setting the formatter to our file handler:
file_handler.setFormatter(formatter)

#Only log ERRORS to the log file:
file_handler.setLevel(logging.ERROR)

#Add multiple handler to a logger:
stream_handler = logging.StreamHandler() #Only display the message format in the console.

#Adding the new handler 'stream_handler' to our logger variable:
logger.addHandler(stream_handler)

#Setting formatter on stream handler:
stream_formatter = logging.Formatter('Displayed By StreamHandler: [%(asctime)s]>[%(levelname)s]>[%(message)s]')
stream_handler.setFormatter(stream_formatter)





class Employee:
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

		logger.info("Created the object: '{}'".format(self.fullname()))
		logger.error("Generated the email: '{}'".format(self.email()))

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def email(self):
		return '{}.{}@email.com'.format(self.last,self.first)


emp_1 = Employee('Henry','Turing',9000)
emp_2 = Employee('Alan','Green',8000)
emp_3 = Employee('Arthur','Smith',7002)

print(emp_3.fullname())
print(emp_2.fullname())
print(emp_1.fullname())
