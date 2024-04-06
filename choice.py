positive = 0
negative = 0
zero = 0

#numbers = int(input("Enter numbers to continue: "))

numbers = 0
while numbers != -1:
	numbers = int(input("Enter numbers to continue: "))

	if numbers == 0:
		zero += 1
	elif numbers > 0:
		positive +=1
	elif numbers < 0 and numbers != -1:
		negative += 1
 

print ("The positive is",positive)
print("The negative is",negative)
print("The zero is",zero)