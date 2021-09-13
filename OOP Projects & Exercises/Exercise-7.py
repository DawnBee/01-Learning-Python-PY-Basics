# OOP Exercise 7: Determine which class a given Bus object belongs to (Check type of an object)

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
	def determine_class(cls):
		condition = issubclass(cls,Vehicle)
		if condition is True:
			print("The class '{}' is a subclass of '{}' class.".format(cls.__name__,Vehicle.__name__))
		else:
			print("The class '{}' don't belong to '{}' class.".format(cls.__name__,Vehicle.__name__))

	@classmethod
	def determine_object(cls,obj):
		condition = isinstance(obj,cls)
		if condition is True:
			print("The object '{}' is an instance of the class '{}'.".format(obj,cls.__name__))
		else:
			print("The class '{}' don't belong to '{}' class.".format(obj,cls.__name__))


class Bus(Vehicle):
	maintenance_charge = 1.10
	def __init__(self,name,max_speed,capacity,comp_name):
		super().__init__(name,max_speed,capacity)
		self.comp_name = comp_name

	def bus_charge(self):
		total_amt = self.fare_charge() * Bus.maintenance_charge
		return total_amt


bus_1 = Bus("Toyota Shuttle",200,50,"Montréal Express")

Bus.determine_object(bus_1)
bus_1.determine_class()
print(type(bus_1))


