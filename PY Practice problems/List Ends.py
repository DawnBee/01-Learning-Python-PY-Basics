# LIST ENDS

'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes 
a new list of only the first and last elements of the given list. For practice, write this code 
inside a function.
'''

a = [5, 10, 15, 20, 25]

b = [12,34,53,73,85,2,44,7,3]

def list_ends(giv_list):

	new_list = [giv_list[0]]

	new_list.insert(1,giv_list[-1])

	return new_list

print(list_ends(a))
print(list_ends(b))

'''
# SOLUTION 2:

def result(giv_list):
	new_list = []

	for n in giv_list:
		if n == giv_list[-1] or n == giv_list[0]:
			new_list.append(n)

	return new_list

print(result(a)) 
print(result(b)) 
'''