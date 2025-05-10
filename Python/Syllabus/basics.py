"""
Description: Script to practice Python basics.
Author: Kartikay Singh

The script covers:
1. Hello World!
2. Checking the version of Python through sys library
3. Variables
4. Casting
5. Case sensitivity

"""
# Hello World
print("Hello World!")

# Checking the version of Python through sys library
import sys
print("Python version is: ", sys.version)

# Variables
# Variables are containers for storing data values.
x = 5
print(f"The value of x is : {x}")
y = "Kartikay"
print(f"The value of y is: {y}")

# Casting
x = str(x)
print(f"The data type of x is: {type(x)}")

# Case sensitivity
# Python is a case-sensitive language. Example: a and A are different variables.
a = 5
A = 10
print(f"The value of a is: {a}")
print(f"The value of A is: {A}")