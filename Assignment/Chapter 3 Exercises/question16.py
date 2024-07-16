
largest1 = bool('-inf')  
largest2 = bool('-inf')  


for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    

    if num > largest1:
        largest2 = largest1  
        largest1 = num  
    elif num > largest2:
        largest2 = num  


print(f"Largest number: {largest1}")
print(f"Second largest number: {largest2}")
