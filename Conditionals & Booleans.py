# IF Statements

if True:
	print("Its True")

var = "a"

if var == "a":
	print("b")

else:
	print("c")


if var == "a":
	print(12)
elif var == "b":
	print(34)
else:
	print(100)


# BOOLEANS 
# and
# or 
# not


# AND

text = 'x'
text2 = True

if text == "x" and text2:
	print("They are Cool!")
else:
	print("They are Hot!")

''' Comparisons:
Equal             | '=='
Not Equal         | '!='
Greater Than      | '>'
Less Than         | '<'
Greater or Equal  | '>=' 
Less or Equal     | '<='
Object Identity   | "is"
'''

# OR

font = 'Arial'

font2 = False

if font == 'Arial' or font2:
	print("They are equal")
else:
	print('''They're Not''')


# NOT
# Switches booleans from 'True' to 'False', likewise.

scroll = "Down"
scroll2 = False

if not scroll2:
	print("Fine")
else:
	print("Not Fine")


# Difference of "==" & "is"

a_list = [1,2,3]
b_list = [1,2,3]

print(a_list == b_list)
print(a_list is b_list)

print(id(a_list))

print(id(b_list))


# Assigning a Zero to a Variable.

h = 0
# If set in any integer the result
# will be "True".


if h:
	print(True)
else:
	print(False)




