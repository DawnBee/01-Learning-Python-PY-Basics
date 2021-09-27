# OOP Exercise 4: Class Inheritance
# Create a Bus class that inherits from the Vehicle class. Give the capacity
# argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
	def __init__(self,name,max_speed,mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

	def seating_capacity(self,capacity):
		return f"The seating capacity of '{self.name}' is {capacity} passengers. "

class Bus(Vehicle):
	def seating_capacity(self,capacity=50):
		return super(). seating_capacity(capacity=50)

vehicle_1 = Bus('School Volvo',180,12)

print(vehicle_1.seating_capacity())