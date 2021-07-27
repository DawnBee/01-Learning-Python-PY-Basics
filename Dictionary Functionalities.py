# DICTIONARY FUNCTIONALITIES

# You can append a list to a value in a dictionary.
student = {"name":'John',"age":25,"courses":['MATH','Science']}

# Access a value from dict.
print(student["name"])

print(student["age"])

# Using the .get() method, to display none,
# if value was not in dict instead of an error. 
print(student.get("school"))

print(student.get("courses"))

# Passing a default/configure value.
print(student.get("school",'Not Found!'))

# Adding entry in dict.
student["phone"] = '555-555'

student["school"] = 'Ontario  University'

print(student)

# Updating values in dict using the .update() method.

student.update({"name":'Jane',"age":23,"phone":'788-222'})

print(student["name"])

print(student)

# Delete entry in dict.
del student["age"]

print(student)

# Pop entries in dict.
student_courses = student.pop("courses")

print(student_courses)

# Loop all keys and values.
print(len(student))

print(student.keys())

print(student.items())

for key,items in enumerate(student,start=1):
	print(key,items)

for key,item in student.items():
	print('{}: {}'.format(key,item))



