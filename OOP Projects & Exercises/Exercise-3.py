# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
	def __init__(self,name,max_speed,mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

	def vehicle_info(self):
		return f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage} "


class Bus(Vehicle):
	pass

vehicle_1 = Bus('School Volvo',180,12)

print(vehicle_1.vehicle_info())