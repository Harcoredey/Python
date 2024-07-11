
account = 0
total = 0


while account != -1:
	deposit = int(input('amount to deposit'))
	total = total+total+deposit
	print("the total balance is: ",total)

	account = int(input('Enter amount withdraw: '))
	account = total -account
	print(account)






