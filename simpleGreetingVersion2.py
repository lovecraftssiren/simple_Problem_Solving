"""
Alexandra Thompson
Jan 23rd 2018
simpleGreetingVersion2.py
This program will ask the user to input a series of information using different
data types. The program will create a custom message to the user.

Notice that even though only a whole number can be someone's age, the entire
program crashes at an incorrect entry. This would not be useful in the
circumstance in which an incorrect entry was accidental.

Another issue is that though the name is a str, a str can still contain 
non-alphabetic characters.
"""

# Get a name from the user and call it name.
name = str(input("What is your name? "))

# Get an age from the user and call it age.
age = int(input("What is your age? "))

# Prints a welcoming statement to the user.
print("\nHi there,", name,"! You are", age, "years old.")
