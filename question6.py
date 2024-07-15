def medical_diagnosis():
    
    input("What is your problem? ")

    
    response = input("Have you had this problem before (yes or no)? ").lower()


    if response == 'yes':
        print("Well, you have it again.")
    elif response == 'no':
        print("Well, you have it now.")
    else:
        print("Invalid response. Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    medical_diagnosis()
