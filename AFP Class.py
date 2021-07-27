class AFP:
	promotion = False
	serial_limit = 4
	breaker = '--------------------'

	def __init__(self,name,rank,branch,SN):
		self.name = name
		self.rank = rank
		self.branch = branch
		self.SN = SN

	def full_info(self):
		print('Name: {}'.format(self.name))
		print('Rank: {}'.format(self.rank))
		print('Branch: {}'.format(self.branch))
		return 'Serial Number: {}'.format(self.SN)

	def is_promote(self):
		if self.rank == 'Private':
			self.promotion = True
		else:
			return False

	def __repr__(self):
		return "AFP('{}','{}','{}','{}')".format(self.name,self.rank,self,branch,self.SN)


	def serial_checker(self):
		serial_num = str(self.SN)
		if len(serial_num) == self.serial_limit:
			return 'Valid'
		else:
			return 'Invalid'

	@classmethod
	def from_string(cls,new_pers):
		name,rank,branch,SN = new_pers.split('+')
		return cls(name,rank,branch,SN)


	@staticmethod
	def list_branch():
		branches = ['Army','Navy','Marines','Airforce']
		return branches

pers_1 = AFP('Andre Taylor','Corporal','Army',8773)
pers_2 = AFP('Scot Colt','Sergeant','Army',3455)
pers_3 = AFP('Andrew Styles','Private','Army',8773)

unlist_pers1 = 'Gilbert Narrow+Sergeant+Navy+9382'
unlist_pers2 = 'Mark Shallow+Captain+Marines+3862'

pers_4 = AFP.from_string(unlist_pers1)
pers_5 = AFP.from_string(unlist_pers2)


class Navy(AFP):
	def __init__(self,name,rank,branch,SN,fleet):
		super().__init__(name,rank,branch,SN)
		self.fleet = fleet

	def __repr__(self):
		return "Navy('{}','{}','{}','{}','{}')".format(self.name,self.rank,self.branch,self.SN,self.fleet)

	def __str__(self):
		return "'{}' is instance of the class 'Navy'.".format(self.name)


pers_6 =  Navy('Steven Stuart','Major','Navy',6327,'7th Fleet')

pers_7 = Navy('Carl Atkinson','Staff Sergeant','Navy',6387,'12th Fleet')


class AirForce(AFP):
	raise_amt = 1.06

	def __init__(self,name,rank,branch,SN,pay):
		AFP.__init__(self,name,rank,branch,SN)
		self.pay = pay

	def pay_raise(self):
		outcome = int(self.pay * self.raise_amt)
		return outcome

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amt = amount

	def __add__(self,other):
		return self.pay + other.pay


pers_8 =  AirForce('Barry Anderson','Lieutenant','AirForce',2493,1500)
pers_9 = AirForce('Tom Bonds','Corporal','AirForce',4928,1200)


class West_Command:

	def __init__(self,first,last,rank,branch):
		self.first = first
		self.last = last
		self.rank = rank
		self.branch = branch

	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	@fullname.setter
	def fullname(self,name):
		first,last = name.split(' ')
		self.firs = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		self.first = first
		self.last =  last
		print('Deleted!')

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first,self.last)

pers_10 = West_Command('Douglas','McArthur','Five-Star General','Army')

pers_11 = West_Command('Steve','Jones','General','Navy')

print(pers_1.full_info())
print(pers_1.is_promote())
print(AFP.breaker)
print(pers_2.full_info())
print(AFP.breaker)
print(pers_6.full_info())
print(AFP.breaker)
print(pers_7.full_info())
print(AFP.breaker)
print(pers_10.fullname)
print(pers_10.email)
pers_10.first = "Tommy"
print(pers_10.fullname)
print(pers_10.email)

print('Thank You Lord!')


