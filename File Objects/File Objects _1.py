# FILE OBJECTS - 1

import os

os.chdir('C:/Users/John/OneDrive/Documents/My Files/Python - Projects/PY Scripts')
print(os.getcwd())


# Opening file objects (NOT RECOMMENDED)
# Reading:
rf = open('File_object_test_file_1.txt','r')
print(rf.read())
# Must be close after opening.
rf.close()

# Writing:
wf = open('File_object_test_file_1.txt','w') 
print(wf.write('Only a Test!'))
# Starts making changes on the assigned position.
wf.seek(13)
print(wf.write('-----> '))
wf.close()

af = open('File_object_test_file_1.txt','a')
print(af.write('[ A Test File ]'))
af.close()

read_all = open('File_object_test_file_1.txt','r')
print(read_all.read())
# Shows current position of what you are reading.
file_position = read_all.tell()
read_all.close()

# Other functionalities:
'''
.mode
.closed
.tell()
.seek()
'''
print(rf.mode)

print(wf.closed)

# Removes unnecessary linebreaks in file.
# print(f_contents,end=" ")

# str format from above file object method .tell()
print('Position: {}'.format(file_position))

