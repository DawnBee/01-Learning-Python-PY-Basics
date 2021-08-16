# LIST OVERLAP

'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this.

2. Write this in one line of Python (don’t worry if you can’t figure 
this out at this point - we’ll get to it soon).
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = [n for n in b if n in a]

print(new_list)


'''
# Solution 2:
import random

rndm_list_1 = []

for n in range(1,11):
  nums = random.randint(1,20)
  rndm_list_1.append(nums)

rndm_list_2 = []

for n in range(1,11):
  nums = random.randint(1,30)
  rndm_list_2.append(nums)


cmn_list_elems = set(rndm_list_1).intersection(set(rndm_list_2))

print('Random List 1:',rndm_list_1)

print('Random List 2:',rndm_list_2)

print(list(cmn_list_elems))
'''

'''
# Solution 3:
set_a = {n for n in a}
set_b = {n for n in b}

common_elem = set_a.intersection(set_b)
print(list(common_elem))
''' 





