# PASSWORD GENERATOR

'''
Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new 
password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or
two from a list.
'''

import string
import random

print("Note: Type 'weak' or 'strong'")

while True:
	weak_pass_list = ['password','Encrypt','key_pass','myPass','loginPass']
	ask_usr = input('Do you want a weak or strong password? ')

	if ask_usr == 'weak':
		weak_pass = random.choice(weak_pass_list)
		print(weak_pass)
	else:
		characters = string.ascii_letters + string.punctuation  + string.digits
		strong_pass =  "".join(random.choice(characters) for x in range(random.randint(8, 30)))
		print(strong_pass)

	import time
	start_time = time.time()
	print("--- %s seconds ---" % (time.time() - start_time))