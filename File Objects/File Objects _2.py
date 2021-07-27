# FILE OBJECTS - 2
# Using Context Manager(RECOMMENDED)

import os

os.chdir('C:/Users/John/OneDrive/Documents/My Files/Python - Projects/PY Scripts')
print(os.getcwd())

divider = "====================================================="

# Reading:
# For small file contents
with open('File_object_test_file_2.txt','r') as read_file:
	rf_contents = read_file.read()
	print(rf_contents)

# Lists all the line in file 
with open('File_object_test_file_2.txt','r') as read_file:
	rf_contents = read_file.readlines()
	print(rf_contents)

# Grabs the first line and will grab the next lines if done multiple times. 
with open('File_object_test_file_2.txt','r') as read_file:
	rf_contents = read_file.readline()
	print(rf_contents,end='')
	print(rf_contents,end='')
	print(rf_contents,end='')

print(divider)

# Iterate over lines in a file
with open('File_object_test_file_2.txt','r') as read_file:
	for line in read_file:
		print(line,end='')

# Specify amount of data to open with 'read' mode
print("\t")
print(divider)

with open('File_object_test_file_2.txt','r') as read_file:
	rf_contents = read_file.read(10)
	print(rf_contents)

print(divider)
# Iterate over small chunks at a time
with open('File_object_test_file_2.txt','r') as read_file:
	size_to_read = 100
	rf_contents = read_file.read(size_to_read)
	print(rf_contents)

print(divider)
with open('File_object_test_file_2.txt','r') as read_file:
	size_to_read = 100
	rf_contents = read_file.read(size_to_read)
	while len(rf_contents) > 0:
		print(rf_contents,end='')
		rf_contents = read_file.read(size_to_read)

# Writing:
with open('File_object_test_file_2.txt','w') as write_file:
	write_file.write(' Among Us')


with open('File_object_test_file_2.txt','a') as append_file:
	append_file.write('\n PVZ')
	append_file.write('\n Candy Crush')


# Using read & write on multiple files a the same time
with open('File_object_test_file_2.txt','r') as read_file:
	with open('File_object_test_file_3.txt','w') as write_file:
		for line in read_file:
			write_file.write(line)

# Copying a picture file:
with open('Warrior.jpg','rb') as read_pic:
	with open('Warrior_copy.jpg','wb') as write_pic:
		for line in read_pic:
			write_pic.write(line)

