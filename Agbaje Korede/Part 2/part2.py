#Pseudocode

#1.Write a program that accepts a sentence with string
#2. Initialize two count variable to 0 for characters and digits 
#3.use a for loop to check through the characters and numbers to count the numbers of characters and digits entered in sentence in no1   
#4.print number of letters and digits of sentence entered in no1.



#print("Enter a sentence: ")
string = (input("Enter a sentence: "))

no_of_letters= 0
no_of_digits = 0
no_of_space = 0
for characters in string:
    if characters>='a' and characters<='z' or characters == " ":
        no_of_letters += 1
    if characters>='0' and characters<='9':
        no_of_digits += 1



print(f'LETTERS:  {no_of_letters} DIGITS:  {no_of_digits}')




