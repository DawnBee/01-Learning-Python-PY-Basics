# INHERITANCE AND CREATING SUBCLASSES

class Employee:
	divider = "==========================================="
	raise_amount = 1.04 

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) 

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('+')
		return cls(first,last,pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Employee('Dean','Winchester',6000)
emp_2 = Employee('Sam','Winchester',5000)
emp_3 = Employee('John','Winchester',3000)

emp_str_1 = "Bob+Singer+8000"
emp_str_2 = "Carl+Green+8500"
emp_str_3 = "Rufus+Black+10000"

'''
# Re-use code by inheriting from parent class:
class Developer(Employee):
	pass
''' 

class Developer(Employee):
	# Changing class variable's value/attribute:
	raise_amount = 7.05

	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

	# You can also use the parent classname here:
		# Employee.__init__(self,first,last,pay)
		# self.prog_lang = prog_lang

dev_1 = Developer('Corey','Schafer',8000,'Python')
dev_2 = Developer('Samantha','Wits',9000,'Java')
dev_3 = Developer('Paul','Hobbit',5000,'C++')

print(dev_1.raise_amount)

print(dev_1.prog_lang)

# Other functionalities:

# Checks if instance belong to a certain class/subclass.
print(isinstance(dev_1,Developer))

# Checks if class is a subclass of another.
print(issubclass(Developer,Employee))

# Shows method resolution order (MRO) and other useful information.
# print(help(Developer))

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

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())

	def email(self):
		return '{}.{}@email.com'.format(self.first,self.last)

mgr_1 = Manager('Sue','Smith',9000,[dev_1,dev_2])

print(mgr_1.email())
mgr_1.print_emps()

print(Employee.divider)

mgr_1.add_emp(dev_3)
mgr_1.print_emps()

print(Employee.divider)

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

