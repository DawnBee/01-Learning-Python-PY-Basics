# OOP Exercise 5: Define property that should have the same value for every class instance

class Vehicle:
	vehicle_color = 'white'
	def __init__(self,name,max_speed,mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

	def seating_capacity(self,capacity):
		return "The seating capacity of {} is {} passengers".format(self.name,self.capacity)

	def general_info(self):
		return "Vehicle Color: {} Vehicle Name: {} Speed: {} Mileage: {}".format(self.vehicle_color,self.name,
			self.max_speed,self.mileage)

class Bus(Vehicle):
	def bus_company(self,comp_name):
		return "'{}' belongs to '{}'".format(self.name,comp_name)

class Car(Vehicle):
	def car_info(self):
		return "Car Name: {} Speed: {}".format(self.name,self.max_speed)


vehicle_1 = Bus('School Volvo',180,12)
vehicle_2 = Bus('Toyota Shuttle',280,19)

vehicle_3 = Car('Toyota Cameroon',190,14)
vehicle_4 = Car('Lamborghini',300,50)

print(vehicle_1.general_info())
print(vehicle_4.general_info())