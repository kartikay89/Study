"""
Description: Module to practice taking inputs in Python.
Author: Kartikay Singh
"""
# Theory:
# input() function is used to take input from the user.

# Take single input

# Ask a user for their name
name = input("Please enter your name: ")
print(f"The name you entered is: {name}")

# Take multiple inputs
firstName, lastName = input("Please enter your first and last name: ").split()
print(f"First Name: {firstName}")
print(f"Last Name: {lastName}")

# Take conditional inputs
# Ask a user for their age
age = int(input("Please enter your age: "))
if age < 18:
    print("You are a minor.")
elif age > 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    
# Ask a user for their email address wihtout @ sign
email, domain = input("Please enter your email address: ").split()
print(f"The email address you entered is: {email}@{domain}.com")
