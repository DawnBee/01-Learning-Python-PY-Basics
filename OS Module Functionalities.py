# OS MODULE FUNCTIONALITIES
import os



divider = "============================================"

# Shows attrib & methods:
print(dir(os))

# Displays current working directory:
print(os.getcwd())

# Changes CWD:
os.chdir("C:/Users/John/OneDrive/Documents/My Files/Python - Projects/PY Scripts")
print(os.getcwd())

# Lists all files in CWD:
print(os.listdir())

# Create new folder in CWD:
'''
os.mkdir("Test_Folder")
# only create the top level directory.

os.makedirs("Test_Folder_2/Sub-test")
# can create multiple sub directories.
'''

# Deleting directories/folders:
'''
os.rmdir("Test_Folder") # RECOMMENDED

os.removedirs("Test_Folder_2/Sub-test")
'''

# Renaming files or folders:
'''
os.mkdir("Test_Folder")

os.rename("Test_Folder","Renamed_Folder")
'''

print(divider)

# Shows info for a file:
print(os.stat("AFP Class.py"))

# Get readable timestamps:
print(divider)
from datetime import datetime

mod_time = os.stat("AFP Class.py").st_mtime

print(datetime.fromtimestamp(mod_time))

print(divider)

# Shows entire directories and files:

# print(os.walk("top"))
''' 
	A generator that yields tuple of three values as it's 
walking the directory TREE, those values are: directory path, 
directories on previous paths, within path and files within 
the path.
'''

'''
for dirpath, dirnames, filenames in os.walk("C:/Users/John/OneDrive/Documents/My Files/Python - Projects/PY Scripts"):
	print(dirpath)
	print(dirnames)
	print(filenames)
'''

# Access Environment Variables: 
#os.environ.get()
#print(os.environ.get('HOME'))

os.environ = "C:/Users/John/OneDrive/Documents/My Files/Python - Projects/PY Scripts"

print(os.environ)


# Create a new file within the 'HOME' Directory:
'''
file_path = os.path.join(os.environ.get('HOME'),'text.txt')
# filename
(os.path.basename('/temp/test.txt'))
# directory
(os.path.dirname('/temp/text.txt'))
# Both:
(os.path.split('/tmp/test.txt'))

'''

'''
# Check existence: 

(os.path.exists('/temp/test.txt'))
(os.path.isdir('/temp/test.txt'))
(os.path.isfile('/temp/test.txt'))
(os.path.splitext('/temp/test.txt'))
'''

print(divider)

# Shows path directories:
print(dir(os.path))

print(divider)

# Shows standard libraries:
print(os.__file__)
