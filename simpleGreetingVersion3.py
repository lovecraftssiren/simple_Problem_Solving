"""
Alexandra Thompson
Jan 23rd 2018
simpleGreetingVersion3.py
This program will ask the user to input a series of information using different
data types. The program will create a custom message to the user.

This program is far more advanced than the first two versions, using while loops,
booleans, exceptions. This is the ideal user friendly program, and while it could
be condensed futher, for the sake of explaining the process, I have chopped it up
and added detailed commentary. Enjoy! 
"""
#Create a boolean to help control flow of program. 
isCorrect = False

#While the correct conditions have not been met... Ask for a name!
while not isCorrect:
    name = str(input("What is your name? "))
    if name.isalpha():
        isCorrect = True
    else:
        print("Sorry, that was not a valid name entry. Please try again.")

#Reset our boolean variable
isCorrect = False

#While the correct conditions have not been met... Ask for an age!
while not isCorrect:
    
    # Because type casting a non number is fatal to the program, let's try asking
    # for age, however, if any errors are raised, we give a prompt and the loop
    # repeats!
    try:
        age = int(input("What is your age? "))
        
        # We might want to raise errors for the purpose of sending it to the reask
        # prompt. For example, if the age is below 0, or too high to be humanly
        # possible.
        if age < 0:
            raise Exception
        if age == 0 or age > 200:
            print("I don't believe that for a second. :) ")
            raise Exception
        
        # In the case that no errors occur, let's exit the loop with our control bool!
        isCorrect = True
        
        # If an error does occur, give a prompt on why, then repeat the loop
    except Exception:
        print("Sorry, that was an invalid age. Please use whole positive numbers only.")

# Prints a welcoming statement to the user.
print("\nHi there,", name,"! You are", age, "years old.")
