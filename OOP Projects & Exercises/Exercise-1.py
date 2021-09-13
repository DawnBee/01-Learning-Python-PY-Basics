# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
	def __init__(self,max_speed,mileage):
		self.max_speed = max_speed
		self.mileage = mileage


vehicle_1 = Vehicle(240,18)

print(vehicle_1.max_speed,vehicle_1.mileage)