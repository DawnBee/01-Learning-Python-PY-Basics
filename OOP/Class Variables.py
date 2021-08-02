# CLASS VARIABLES

''' 
class variable = are variables that are shared among all
instances in a class.
''' 

divider = "==============================================="

class Employee:
	raise_amount = 1.04 #Class Variable Example

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) #We can also call the class here instead of 'self'.


emp_1 = Employee('Dean','Winchester',6000)
emp_2 = Employee('Sam','Winchester',5000)
emp_3 = Employee('John','Winchester',3000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Access from class and instances:
print(Employee.raise_amount)
print(emp_1.raise_amount)

emp_1.raise_amount = 1.09

print(emp_1.raise_amount)

# Display class/instance namespace:
print(emp_2.__dict__)
print(divider)
print(Employee.__dict__)
print(divider)

# Setting new values for class variables:
class Flowers:
	temp_raise_amt = 5

	def __init__(self,name,habitat,climate,req_temp,season):
		self.name = name
		self.habitat = habitat
		self.climate = climate
		self.req_temp = req_temp
		self.season = season

	def apply_temp_raise(self):
		self.req_temp = int(self.req_temp * self.temp_raise_amt /3) 


	def display_temp(self):
		return '{}° Celsius'.format(self.req_temp)


flower_1 = Flowers('Cacti Flowers','Dessert','Tropical',29,'Rainy & Dry')
flower_2 = Flowers('Early Buttercup','Savanna','Tropical & Sub Tropical',10,'Rainy & Dry')
flower_3 = Flowers('Artic Poppy','Tundra','Polar',15,'Rainy & Dry')

# Changing class variable using 'class' name:
Flowers.temp_raise_amt = 3

# Changing class variabe to a particular instance/object:
emp_3.temp_raise_amt = 6

flower_2.apply_temp_raise()
print(flower_2.req_temp)

print(flower_2.temp_raise_amt)
print(flower_2.display_temp())

print(emp_3.temp_raise_amt)
print(Flowers.temp_raise_amt)

print(divider)

# Situations when it's not logical to use 'self' to a class variable:
# If values are the same for all instances within class.

class Workers:
	num_workers = 0
	def __init__(self,f_name,l_name,salary):
		self.f_name = f_name
		self.l_name = l_name
		self.salary = salary

		Workers.num_workers += 1

wrkr_1 = Workers('Tyron','Jennings',900)
wrkr_2 = Workers('Elsa','Queen',500)
wrkr_3 = Workers('Alice','Dancing',300)
wrkr_4 = Workers('Edward','Wood',800)

# Since the class variable here is incremented everytime
# an object is created, it is necessary to call the class name, instead
# of the instance name.
print(Workers.num_workers,'workers')
