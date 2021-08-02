# CLASSES & VARIABLES

'''
Method = Function
Attribute = Data
Object/Instance = Variable
'''

# Manual Assigning:
class Employee: 
	pass

emp_1 = Employee()

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@gmail.com'
emp_1.pay = 5000

print(emp_1.first,emp_1.last)

print(emp_1.email)

# Automatic Assigning:
class Dragons:
	def __init__(self,habitat,rarity,nick_name):
		self.habitat = habitat
		self.rarity = rarity
		self.nick_name = nick_name

	def full_info(self):
		return '{2}: {0} Habitat, {1}'.format(self.habitat,self.rarity,self.nick_name)

drag_1 = Dragons('Terra','Common','Tiny')
drag_2 = Dragons('Flame','Common','Luz')
drag_3 = Dragons('Sea','Heroic','Godzilla')

print(drag_3.habitat)
print(drag_1.nick_name)
print(drag_2.full_info())

