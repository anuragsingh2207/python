# Same nume variables but with different scope

def retrun_string():
    string = "Inside function Local Variable"
    return string
    
    
string = "Outside function Global Variable"

print("\n+++First Program+++")

print(string)

print(retrun_string())
print("\n\n")


#Using Global variable within the function scope

def print_var():
    print(ex1)


ex1 = "Global Variable"
print("+++Second Program+++")
print_var() 


#Same name of varaibles but in different scope

def sum(a, b):
    sum = a + b
    return sum

a = 2 
b = 3 

print("\n+++Third Program+++")
print("Sum of a & b is: "+str(sum(a,b)))