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

# Comments

# This is a single line comment

# This is a single line comment
# splitted into multiple
# lines

"""
This is a multi-line comment
This can be splitted into 
multiple lines
Python ingnores them on run time.
Unless they are in a variable.
"""

# variables continued
x = 5
print(f"The values of x is: {x} and the data type is: {type(x)}")

# Casting
# string type
x = str(x)
print(f"The value of x is: {x} and the data type is: {type(x)}")

# float type
x = float(x)
print(f"The value of x is: {x} and the data type is: {type(x)}")

# Assigning multiple values to multiple variables
first_name, last_name, age = "Kartikay", "Singh", 35
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Age: {age}")

# Assigning single value to multiple variables
x = y = z = "Kartikay"
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# Unpacking a collection

# list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# tuple
fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# set
fruits = {"apple", "banana", "cherry"}
x, y, z = fruits
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# Dictionary
fruits = {"apple": 1, "banana": 2, "cherry": 3}
x, y, z = fruits
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# Global variables
x = "Kartikay"

def names():
    print(f"Hello {x}")

# calling the function
names()

# Declaring global variable inside a function
def names():
    global x 
    x = "Singh"
    print(f"Hello {x}")

# calling the function
names()

# Since global x is declared inside the function, it will be overwritten.
print(f"Hello {x}")