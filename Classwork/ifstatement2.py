age = int(input('enter age: '))
if age >= 19 and age <= 45:
	print("you are eligible to make your own decisions")
elif age > 13 and age <= 19:
	print("you are a teenager")
elif age > 0 and age <= 13:
	print('you are still a child')

else:
	print("you are old")