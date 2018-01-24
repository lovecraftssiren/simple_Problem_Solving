"""
Alexandra Thompson
Jan 23rd 2018
simpleGreeting.py
This program will ask the user to input a series of information using different
data types. The program will create a custom message to the user.

Notice this program works great, only if however the input is geniune to the
question. This program can be easily be abused as letters are a valid input for
the name variable and numbers and symbols can be a part of someone's name.
"""

# Get a name from the user and call it name.
name = input("What is your name? ")


# Get an age from the user and call it age.
age = input("What is your age? ")

# Prints a welcoming statement to the user.
print("\nHi there,", name,"! You are", age, "years old.")

