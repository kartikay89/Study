"""
Description: Module to practice string operations in Python.
Author: Kartikay Singh
"""
# Theory: 
# Strings are a sequence of characters enclosed in single or double quotes. Example: "Hello World", 'Hello World'

# Strings in single quotes, single line
singleQuotesString = 'Hello World'
print(f"This is an example of single quotes string: {singleQuotesString}")

# Strings in double quotes, single line
doubleQuotesString = "Hello World"
print(f"This is an example of double quotes string: {doubleQuotesString}")

# Multiline strings, single quotes
multiLineSingleQuotesString = '''This is an example of
multiline string in single quotes.'''
print(f"This is an example of multiline string in single quotes: {multiLineSingleQuotesString}")

# Multiline strings, double quotes
multiLineDoubleQuotesString = """This is an example of
multiline string in double quotes."""
print(f"This is an example of multiline string in double quotes: {multiLineDoubleQuotesString}")

# Strings as Arrays
a = "Hello World"
print(f"The first character of the string is: {a[0]}")
print(f"The last character of the string is: {a[-1]}")

# Loop through the string
string = "Hello World"
for i in string:
    print(i, end="")

# String Length
string = "Hello World"
print(f"\nThe length of the string is: {len(string)}")

# Check a string for a value
string = "Hello World"
print("W" in string)

# Check based on conditional statements
if "World" in string:
    print("The string contains the word 'World'")
else:
    print("The string does not contain the word 'World'")

# Check on NOT condition
print("Expensive" not in string)
if "Expensive" not in string:
    print("The string does not contain the word 'Expensive'")
else:
    print("The string contains the word 'Expensive'")
    
# String slicing
string = "Hello World"
print(f"The characters from 2 to 5(excluding) of the string are: {string[2:5]}")
print(f"The characters from 2 to end of the string are: {string[2:]}")
print(f"The characters from start to 5(excluding) of the string are: {string[:5]}")
print(f"The characters from the back of the string are: {string[:-1]}")

# Modifying strings

# upper() method
string = "Hello World"
print(f"The string is modified from {string} to upper case like this: {string.upper()}")

# lower() method
string = "Hello World"
print(f"The string is modified from {string} to lower case like this: {string.lower()}")

# Remove whitespace
string = " Hello World "
print(f"The string is modified from {string} to remove whitespace like this: {string.strip()}")

# replace() method
string = "Hello World"
print(f"The string is modified from {string} to replace 'World' with 'Python' like this: {string.replace('World', 'Python')}")

# split() method
string = "Hello World"
print(f"The string is modified from {string} to split the string like this: {string.split(' ')}")
