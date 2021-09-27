from functools import wraps

#Decorators
def html_tag(tag):
	def wrap_text(msg):
		print("<{0}> {1} </{0}>".format(tag,msg))
	return wrap_text


def dec_func(original_func):
	def wrapper_function(*args,**kwargs):
		print('Prints this before executing the {}'.format(original_func.__name__))
		return original_func(*args,**kwargs)
	return wrapper_function


def timer(orig_func):
	import time as t 
	@wraps(orig_func)
	def wrapper(*args,**kwargs):
		
		t1 = t.time()
		exec_func = orig_func(*args,**kwargs)
		t2 = t.time() - t1
		print("Ran with '{}' and took {:.3f} sec to execute".format(orig_func.__name__,t2))

		return exec_func
	return wrapper


def logger(original_func):
	import logging

	logger = logging.getLogger()
	logger.setLevel(logging.INFO)
	
	formatter = logging.Formatter('[%(levelname)s] {%(asctime)s} %(message)s')
	stream_formatter = logging.Formatter('[%(message)s]')

	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(stream_formatter)

	file_handler = logging.FileHandler('employees.log')
	file_handler.setLevel(logging.DEBUG)
	file_handler.setFormatter(formatter)
	
	logger.addHandler(file_handler)
	logger.addHandler(stream_handler)

	@wraps(original_func)
	def wrapper_function(*args,**kwargs):
		logger.info('Logged: {}'.format(*args,**kwargs))
		logger.debug('Logged: {}'.format(*args,**kwargs))
		return original_func(*args,**kwargs)
	return wrapper_function


#Decorator Class
class raise_info(object):
	def __init__(self,orig_func):
		self.orig_func = orig_func

	def __call__(self,*args,**kwargs):
		print('NOTE: New amount had been set to raise_amount!')
		return self.orig_func(*args,**kwargs)




#Parent Class
class Employee:
	import logging
	raise_amount = 1.09
	logging.basicConfig(filename="employees.log",level=logging.INFO,format='[%(levelname)s] {%(asctime)s} %(message)s')

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

		# Employee.logging.info("Created the object '{}'.".format(self.fullname))

	@property
	def fullname(self):
		return "{} {}".format(self.first,self.last)

	@fullname.setter
	def fullname(self,name):
		first,last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		self.first = ''
		self.last = ''
		print('Not Found')

	def email(self):
		return f"{self.first}.{self.last}@gmail.com"

	@logger
	def __repr__(self):
		return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

	def __str__(self):
		return "{} is an instance of the class 'Employee'.".format(self.fullname)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	@raise_info
	def set_raise_amt(cls,other):
		cls.raise_amount = other

	@classmethod
	def from_string(cls,name):
		first,last,pay = name.split('ç')
		return cls(first,last,pay)

	@staticmethod
	@timer
	def is_today_workday():
		from datetime import date
		import time as t
		t.sleep(1.2)
		curr_day = date.today()
		if curr_day.weekday == 5 or curr_day.weekday() == 6:
			print ("The date is: {:%B %d, %Y (%A)} and it falls on weekend!".format(curr_day))
		print ("The date is: {:%B %d, %Y (%A)} and its working day!".format(curr_day))
		
	@staticmethod
	def is_workday(day):
		import datetime
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp_1 = Employee('Mark','Hamberg',8000)
emp_2 = Employee('James','Anderson',5000)
emp_3 = Employee('George','Burns',2000)

string_emp_1 = "TrevorçBoltsç6000"
string_emp_2 = "HannahçCollinsç4000"
string_emp_3 = "KevinçWhiteç6000"

emp_4 = Employee.from_string(string_emp_1)
emp_5 = Employee.from_string(string_emp_2)
emp_6 = Employee.from_string(string_emp_3)

class Developer(Employee):
	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

	def dev_spec(self):
		if self.prog_lang == "Html":
			print("{} is in charge of front-end developing".format(self.fullname))
		elif self.prog_lang == "Java":
			print("{} is in charge of back-end developing".format(self.fullname))
		else:
			print("{} is a full-stack developer".format(self.fullname))

dev_1 = Developer('Brad','Schiff',8000,'Html')
dev_2 = Developer('Ania','Kubów',9000,'Java')
dev_3 = Developer('Corey','Schafer',10000,'Python & Java')

class Manager(Employee):

	def __init__(self,first,last,pay,employees=None):
		Employee.__init__(self,first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def rem_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def disp_emps(self):
		for emp in self.employees:
			print("--> {}".format(emp.fullname))

mngr_1 = Manager('Mark','Zuckerberg',60000,[dev_1,dev_2,dev_3])

