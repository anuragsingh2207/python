'''
Create a variable and assign it the string "Just do it!"

Access the "!" from the variable by index and print() it

Print the slice "do" from the variable

Get and print the slice "it!" from the variable

Print the slice "Just" from the variable

Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
'''

text = "Just do it!"

print(text[10])
print(text[5:7])
print(text[8:])
print(text[:4])
print(text[5:])
slice = text[5:]
final = "Don't " + slice
print("Sliced & Concatenated String",final)