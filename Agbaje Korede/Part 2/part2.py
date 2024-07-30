#Write a program that accepts a sentence and 
#calculate the number of letters and digits. 
#Suppose the following input is supplied to the 
#program: hello world! 123 Then, the output 
#should be: LETTERS 10 DIGITS 3

#Pseudocode
#1. prompt user to enter a string 
#2. Initialize the two count variables to 0.
#3. Use a for loop to traverse through the characters in #the string and increment the first count variable each #time a digit is encountered and increment the second count #variable each time a character is encountered.
#4. Print the total count of both the variables.

#print("Enter a sentence: ")
#string = input()
string = (input("Enter a sentence: "))

no_of_letters= 0
no_of_digits = 0

for characters in string:
    if characters>='a' and characters<='z':
        no_of_letters += 1
    if characters>='0' and characters<='9':
        no_of_digits += 1


printf("{LETTERS: ", no_of_letters} {"DIGITS: ", no_of_digits})




