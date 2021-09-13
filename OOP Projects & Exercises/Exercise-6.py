# OOP Exercise 6: Class Inheritance

'''
Given:

Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle
is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() 
method of a Vehicle class in Bus class. Use the following code for your parent Vehicle class. We need to access the parent
class from inside a method of a child class.
'''

class Vehicle:
	def __init__(self,name,max_speed,capacity):
		self.name = name
		self.max_speed = max_speed
		self.capacity = capacity

	def fare_charge(self):
		return self.capacity * 100

class Bus(Vehicle):
	maintenance_charge = 1.10

	def bus_charge(self):
		total_amt = self.fare_charge() * Bus.maintenance_charge
		return total_amt

	def disp_charge(self):
		return "Total bus fare is: {:.0f}".format(self.bus_charge())


vehicle_1 = Bus('School Volvo',180,50)

print(vehicle_1.disp_charge())