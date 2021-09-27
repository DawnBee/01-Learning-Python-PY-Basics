# CSV MODULE
# CSV --> Comma Separated Values.

import csv

'''
inorder to read,write and modify a csv file we must first 
import the CSV module from the library. 
'''


# Opening a CSV file:
with open('Cartoon_info.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader: #w/o a for loop it won't display the contents, for it acts like a generator.
		print(line)


# Specifying an index for fieldnames:
with open('Cartoon_info.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		print(line[2]) #Index of the 'email' fieldname.


# Step over values:
with open('Cartoon_info.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)

	next(csv_reader) #Skips the first line.

	for line in csv_reader:
		print(line[0])


# Read & Write on CSV file:
'''
In this example the delimiter is change to
a hyphen ('-') instead of commas.
'''
with open('Cartoon_info.csv','r') as csv_file: #Read Mode
	csv_reader = csv.reader(csv_file)
	with open('Cartoon_info(2).csv','w') as new_file: #Write Mode
		csv_writer = csv.writer(new_file,delimiter='$')

		for line in csv_reader:
			csv_writer.writerow(line) #Write each line from 'Cartoon_info.csv' to new_file.


# Opening the new csv file we created by specifying the 
# delimiter we passed.
with open('Cartoon_info(2).csv','r') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter='$') #w/o the delimiter specified it will not be parse correctly.

	for line in csv_reader:
		print(*line) #'*' unpacks the list 'line'.


# Using dictionary reader/writer:
# (RECOMMENDED)
'''
In this approach the fieldnames become the key for the
dictionary and the value will be the field's data.
'''
with open('Cartoon_info(3).csv','r') as csv_file:
	csv_reader = csv.DictReader(csv_file,delimiter='¶')

	for line in csv_reader:
		print(line['email']) #Access a particular key from the dictionary, then prints only its values.


# Dictionary Writer
with open('Cartoon_info.csv','r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	with open('Cartoon_info(4).csv','w') as new_file:
		fieldnames = ['first_names','last_names','email']
		csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')

		csv_writer.writeheader() #Displays fieldnames above data/values

		for line in csv_reader:
			csv_writer.writerow(line)


# Moving a particular fieldname and it's data:
with open('Cartoon_info.csv','r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	with open('New_cartoon_info.csv','w') as new_file:
		fieldnames = ['first_names','last_names'] #Don't include the 'email' fieldname here.
		csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			del line['email'] #Deletes the data of the 'email' fieldname.
			csv_writer.writerow(line)

