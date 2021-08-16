# LIST REMOVE DUPLICATES

'''
Write a program (function!) that takes a list and returns a new list that contains all 
the elements of the first list minus all the duplicates.

Extras:

1. Write two different functions to do this - one using a loop and constructing a list, and 
another using sets.

2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

a = [2,1,43,23,6,78,12,3,1,9,6]

b = [2,12,56,24,68,6,21,43,1,23]

# Solution 1:
def for_loop_rem_dupli(giv_list_1,giv_list_2):
	new_list = []
	for n in giv_list_2:
		if n in giv_list_1:
			new_list.append(n)

	return new_list

print(for_loop_rem_dupli(a,b))


# Solution 2:
def set_rem_dupli(set_1,set_2):
	comm_elm = set(set_1).intersection(set(set_2))

	return (list(comm_elm))

print(set_rem_dupli(a,b))


# Solution 3:
def set_compre_rem_dupli(set_1,set_2):
	comm_elm = {n for n in set_2 if n in set_1}

	return(list(comm_elm))

print(set_compre_rem_dupli(a,b))
