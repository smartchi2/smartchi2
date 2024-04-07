total_number = 0

for number in range (10):
	scores = int(input("Enter your scores: "))
	total_number = total_number + scores
        

average = total_number / 10
print(f"total scores is {total_number}")
print(f" average is {average}")