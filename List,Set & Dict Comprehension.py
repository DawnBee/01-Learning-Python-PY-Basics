# LIST,SET & DICT COMPREHENSION

divider = "----------------------------------------------"

num_list = [1,2,3,4,5,6,7,8,9]

for_list = []

#LIST

# Using For Loop:
for n in num_list:
	for_list.append(n)

print(for_list)

print(divider)

# List Comprehension:
compre_list = [n for n in num_list]

print(compre_list)

print(divider)

# Using For Loop:
for_list_2 = []
for n in num_list:
	for_list_2.append(n*n)
print(for_list_2)

print(divider)

# List Comprehension:

compre_list_2 = [n*n for n in num_list]

print(compre_list_2)	

print(divider)

for_list_3 = []

# Using For Loop:
for n in num_list:
	if n % 2 == 0:
		for_list_3.append(n)
print(for_list_3)

print(divider)

# List Comprehension:
compre_list_3 = [n for n in num_list if n % 2 == 0]

print(compre_list_3)

print(divider)

# Using For Loop:
for_list_4 = []

for letter in 'abcd':
	for num in range(1,6):
		for_list_4.append((letter,num))

print(for_list_4)

print(divider)

# List Comprehension:

compre_list_4 = [(letter,num) for letter in 'abcd' for num in range(1,6)]

print(compre_list_4)

print(divider)

# DICTIONARY 

# Using For Loop:
for_dict = {}
names = ['Bruce','Clark','Peter','Wade','Logan']
heros = ['Batman','Superman','Spiderman','Deadpool','Wolverine']


for name,hero in zip(names,heros):
	for_dict[name] = hero

print(for_dict)

print(divider)

# Dict Comprehension:

dict_compre = {name:hero for name,hero in zip(names,heros)}

print(dict_compre)

print(divider)

# SET 

# Using For Loop:
nums = [12,34,1,2513,236,325,42,2,1,12,42]

for_set = set()

for n in nums:
	for_set.add(n)

print(for_set)

print(divider)

# Set Comprehension:
set_compre = {n for n in nums}

print(set_compre)

print(divider)

# GENERATOR EXPRESSIONS

# Generator using For Loop:
num_list_2 = [9,75,5,3,12,1,6]

def gen_func(num_list_2):
	for n in num_list_2:
		yield n*n

for_gen = gen_func(num_list_2)

for i in for_gen:
	print(i)

print(divider)

# Generator Comprehension:
gen_compre = (n*n for n in num_list_2)

for i in gen_compre:
	print(i)

print(divider)

# USING MAP+LAMBDA FUNCTIONS

lamb_list = [1,6,32,3,26,62,13]

map_list = map(lambda n: n*n, lamb_list)

for i in map_list:
	print(i)

print(divider)

# USING FILTER+LAMBDA FUNCTIONS

filter_list = filter(lambda n: n%2 == 0,lamb_list)

for i in filter_list:
	print(i)

