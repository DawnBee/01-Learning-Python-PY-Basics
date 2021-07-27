# SORTING LISTS,TUPLES & OBJECTS


# Sorting Lists
a_list = [4,5,6,8,34,36,85,21,51]

# Using sorted() method
sort_list = sorted(a_list)

print('Unsorted: ', a_list)

print('Sorted: ', sort_list)

# descending
sort_list = sorted(a_list,reverse=True)
print(sort_list)

# ascending
sort_list = sorted(a_list)
print(sort_list)

# Using sort() method
# Sorts place in place and return none.

a_list.sort(reverse=True)

print(a_list)

a_list.sort()

print(a_list)

''' sorted() VS. .sort()
-gives more  | -best in working
flexibility. |  with list, to sort
-we can pass |  it in place.
iterables.   |
'''

# Sorting Tuples

b_tuple = (9,8,7,6,5,4,3,2,1)

# ascending
sort_tup = sorted(b_tuple)

print(sort_tup)

# descending
sort_tup = sorted(b_tuple,reverse=True)

print(sort_tup)

# Sorting Dictionary

alph_dict = {'a':1,'d':4,'b':2,'z':26,'c':3}

sort_dict = sorted(alph_dict)

print(sort_dict)

sort_dict = sorted(alph_dict,reverse=True)

print(sort_dict)

# Sorting base on absolute values

list_integers = [-2,5,-78,-1,6,7,8]

list_integers.sort(key=abs)

print(list_integers)

sort_integers = sorted(list_integers,key=abs)

print(sort_integers)

# Object Oriented Sorting

class Employee:
	def __init__(self,name,age,pay):
		self.name = name
		self.age = age
		self.pay = pay

	def __repr__(self):
		return '{} {} {}'.format(self.name,self.age,self.pay)	

e1 = Employee('Carl',37,7000)
e2 = Employee('Sarah',29,8000)
e3 = Employee('John',43,9000)

def name_sort(emp):
		return emp.name

def age_sort(emp):
		return emp.age

def pay_sort(emp):
		return emp.pay

employee_list = [e1,e2,e3]

sorted_name = sorted(employee_list,key=name_sort)

sorted_age = sorted(employee_list,key=age_sort)

sorted_pay = sorted(employee_list,key=pay_sort)

print(sorted_name)
print(sorted_age)
print(sorted_pay)


print("===========================================")
# Sorting object using Lambda function

lamb_sort_name = sorted(employee_list,key=lambda emp: emp.name)

lamb_sort_age = sorted(employee_list,key=lambda emp: emp.age)

lamb_sort_pay = sorted(employee_list,key=lambda emp: emp.pay)

print(lamb_sort_name)
print(lamb_sort_age)
print(lamb_sort_pay)

print("===========================================")
# Sorting object using attrgetter

from operator import attrgetter as atg

getter_sort_name = sorted(employee_list,key=atg('name'))
getter_sort_age = sorted(employee_list,key=atg('age'))
getter_sort_pay = sorted(employee_list,key=atg('pay'))

print(getter_sort_name)
print(getter_sort_age)
print(getter_sort_pay)

