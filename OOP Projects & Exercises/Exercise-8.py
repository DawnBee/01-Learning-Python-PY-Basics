# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
	def __init__(self,name,max_speed,capacity):
		self.name = name
		self.max_speed = max_speed
		self.capacity = capacity

	def fare_charge(self):
		return self.capacity * 100

	def __repr__(self):
		return "Vehicle('{}','{}','{}')".format(self.name,self.max_speed,self.capacity)

	def __str__(self):
		return '{}'.format(self.name)

	@classmethod
	def determine_object(cls,obj):
		condition = isinstance(obj,cls)
		if condition is True:
			print("The object '{}' is an instance of the class '{}'.".format(obj,cls.__name__))
		else:
			print("The class '{}' don't belong to '{}' class.".format(obj,cls.__name__))

class Bus(Vehicle):
	pass


School_bus = Bus('School Volvo',180,50)

Vehicle.determine_object(School_bus)