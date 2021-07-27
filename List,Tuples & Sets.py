# LIST

num_list = [1,2,3,4,5,6,7,8,9]

alph_list = ['b','c','d','e','f','g']

greek_alph = ['alpha','beta','gamma','omega']

unsrt_list = [124,5,151,135,64,25,124,12]

print(len(num_list))

print(num_list[0])

print(num_list[1])

print(num_list[0:6])

print(num_list[0:6:2])

num_list.append('a')

num_list.insert(0,'a')

print(num_list)

num_list.extend(alph_list)

num_list.remove('a')

print(num_list)

popped = num_list.pop()

print(num_list)

print(popped)

num_list.reverse()

print(num_list)

#ascending
unsrt_list.sort()
print(unsrt_list)

#descending
unsrt_list.sort(reverse=True)

print(unsrt_list)

sort_list = sorted(unsrt_list)

print(sort_list)

print(unsrt_list)

print(min(unsrt_list))

print(max(unsrt_list))

print(sum(unsrt_list))

#reversed
print(num_list.index('c'))

print(25 in unsrt_list)

for nums in unsrt_list:
	print(nums)

for index, nums in enumerate(unsrt_list):
	print(index, nums)

for index, nums in enumerate(unsrt_list, start=2):
	print(index,nums)

for index,nums in enumerate(num_list, start=-1):
	print(index,nums)

join_list = '+'.join(greek_alph)

print(join_list)

split_list = join_list.split('+')

print(split_list)


# TUPLE (Immutable)
# Uses parenthesis, does not support item assignment.

tis_tuple = ('dog','cat','bird')

print(tis_tuple)	


# SETS
# Uses curly brackets.
# Removes Duplicates.
# Order can change.
# Works effeciently in "Membership Test".

drag_elem = {'Terra','Flame','Dark','Terra','Sea'}

drag_rarity_1 = {'Legendary','Common','Very Rare','Rare','Common'}

drag_rarity_2 = {'Heroic','Epic','Very Rare','Rare','Common'}

# Shows values that are present to both sets.
print(drag_rarity_1.intersection(drag_rarity_2))	

# Shows values that are absent to both sets.
print(drag_rarity_1.difference(drag_rarity_2))	
print(drag_rarity_2.difference(drag_rarity_1))	

# Joins all the values from set1 to set2
print(drag_rarity_1.union(drag_rarity_2))

''' Empty List
	empty_list = []
	empty_list = list()
	
	Empty Tuple
	empty_tuple = ()
	empty_tuple = tuple()

	Empty Set
	empty_set = set()
'''
