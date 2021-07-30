# IMPORTING MODULES

divider = "============================================"

# Must be on the same directory.
import my_module as mm

result = mm.cube_num(96)

print(result)

# Importing specific functions:
from my_module import cube_num

result_2 = cube_num(34)

print(result_2)

# Importing multiple variables and functions:
from my_module import cube_num,func_info

print(func_info)

# Adding shortcut name:
from my_module import cube_num as cn

result_3 = cn(56)

print(result_3)

# Importing everything from the module:
from my_module import *
# The "star" means everything.

# Show lists of directories for modules:
import sys

print(sys.path)

print(divider)

# Manually add a directory to sys.PATH:
sys.path.append('C:\\Users\\John\\OneDrive\\Documents\\My Files\\Python - Projects\\PY Scripts')

print(sys.path)

''' for more advance 'directory adding' in windows & 
macintosh watch YT tutorials. '''

# Few Module samples that may come in HANDY:
'''
import random
import math
ímport os
import datetime
import calendar
'''






