
#admin_type = ["Primary Admin","Full Access Admin","Signatory Admin","Limited Access Admin","HR Admin"]
#client_type = ["Fixers","Survivors","Protectors"]

class Admin:
	raise_amount = 1.05
	authorize_personel = False

	def __init__(self,first_name,last_name,admin_type,client_type,salary):
		self.first_name = first_name
		self.last_name = last_name
		self.admin_type = admin_type
		self.client_type = client_type
		self.salary = salary

	@property
	def fullname(self):
		return '{} {}'.format(self.first_name,self.last_name)

	def full_info(self):
		return '{}:{} --> {}'.format(self.last_name,self.admin_type,self.client_type)

	def email(self):
		return '{}.{}@bus_company.com'.format(self.first_name,self.last_name)

	def apply_raise(self):
		self.salary = int(self.salary * self.raise_amount)

	def __repr__(self):
		return '''Admin('{}','{}','{}','{}','{}')'''.format(self.first_name,self.last_name,self.admin_type,
			self.client_type,self.salary)

	
	def __str__(self):
		return '{} -> {}'.format(self.fullname,self.salary)


	@property
	def is_authorize(self):
		if self.admin_type == "Primary Admin":
			self.authorize_personel = True
			return True
		else:
			return False

	@classmethod
	def set_raise_amount(cls,amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls,pers_str):
		first_name,last_name,admin_type,client_type,salary = pers_str.split('-')
		return cls(first_name,last_name,admin_type,client_type,salary)

pers_1 = Admin("John","Smith","Full Access Admin","Survivors",5000)
pers_2 = Admin("Mark","Anderson","Primary Admin","Protectors",5500)
pers_3 = Admin("Dave","Green","Signatory Admin","Fixers",3000)
pers_4 = Admin("Peter","Woods","Limited Access Admin","Fixers",3000)

pers_str_1 = 'Michael-Angelo-HR Admin-Fixers-2400'
pers_str_2 = 'Dona-tello-Limited Access Admin-Fixers-1400'
pers_str_3 = 'Leon-Ardo-Limited Access Admin-Protectors-1400'
pers_str_4 = 'Raph-Ael-Limited Access Admin-Protectors-1400'


print(pers_1)

pers_5 = Admin.from_string(pers_str_1)
pers_6 = Admin.from_string(pers_str_2)

print(pers_6.fullname)
print(pers_6.full_info())
print(pers_6.email())