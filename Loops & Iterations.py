# LOOPS & ITERATIONS
# Break
# Continue
# For Loops
# Nested For Loops
# While Loops

divider = "---------------"
num_list = [1,2,3,4,5]

#FOR LOOPS
for num in num_list:
	print(num)

print(divider)

# BREAK

for n in num_list:
	print(n)
	if n == 3:
		print("a")
		break

# CONTINUE

print(divider)

for n in num_list:
	if n == 2:
		print("a")
		continue
	print(n)

# NESTED FOR LOOPS
print(divider)

for n in num_list:
	for i in "abc":
		print(n,i)

print(divider)

for j in range(-10,11):
	print(j)

# WHILE LOOP
# Will keep going until a condition is met, or
# hit a break.

print(divider)

x = 0

while x < 11:
	print(x)
	x += 1

print(divider)
# BREAK

y = 0

while y < 10:
	if y == 5:
		break
	print(y)
	y += 1

print(divider)

z = 0

while True:
	if z == 12:
		break
	print(z)
	z += 1
