def max_of_two(x, y):
	if x > y:
		return x
	else:
		return y

max_1 = max_of_two(5,4)
max_2 = max_of_two(-2,-3)
max_3 = max_of_two(0,0)

print(max_1)
print(max_2)
print(max_3)

def max_of_three(x, y, z):
	if x >= y and x >= z:
		return x
	elif y >= x and y >= z:
		return y
	else:
		return z

max_4 = max_of_three(5,4,7)
max_5 = max_of_three(-2,-3,-1)
max_6 = max_of_three(0,0,0)

print(max_4)
print(max_5)
print(max_6)