from platform import python_branch
import string
from typing import Concatenate


print("Python Print with double quotes")
print('Python Print with single quotes')

# empty string
s1 = ""
s2 = '1984!'
s3 = "@!#$%^&*()"
s4 = "Hello World"

# String Index starts with 0 and goes up by one from left to right 
s5 = "012345"

# Accessing Index of a String 
ex_8 = "orange"
print(ex_8[2])

print("apple"[4])


# String Slicing
ex_10 = "apricots"

print(ex_10[:3])  # Slice from 0th to 3rd index
print(ex_10[2:5]) # Slice from 2nd to 5th index
print(ex_10[4:])  # Slice from 4th index to last

# String Concatenation
concatenated = "R2" + "-" + "D2"

print(concatenated)
print(concatenated[3])
print(concatenated[1:4])


unchanged = "forrest gump"
sliced = unchanged[6:]

print("Sliced String:",sliced)
print("Unchanged String:",unchanged)
print("Sliced String:",unchanged[10])
print("Unchanged String:",unchanged)




 