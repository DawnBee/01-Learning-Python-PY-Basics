# LIST OVERLAP COMPREHENSIONS

'''
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require
the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between
the lists (without duplicates). Make sure your program works on two lists of different sizes. 
Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions
from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python, 
but a few readers pointed out that this was impossible to do without using sets that I had not yet 
discussed on the blog, so you can either choose to use the original directive and read about the set 
command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

• Randomly generate two lists to test this
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Solution 1:
set_comm_elems = {n for n in a if n in b}
print(list(set_comm_elems))

# Solution 2:
common_elems = set(a).intersection(set(b))
print(list(common_elems))

# Solution 3:
import random as rn

new_list_1 = []

for i in range(1,11):
	rand_nums =  rn.randint(1,15)
	new_list_1.append(rand_nums)

new_list_2 = []

for i in range(1,11):
	rand_nums = rn.randint(1,10)
	new_list_2.append(rand_nums)

rand_comm_elems = set(new_list_1).intersection(set(new_list_2))

print(list(rand_comm_elems))