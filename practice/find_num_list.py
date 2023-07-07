
x = list(map(int, input("Enter list values: ").split())) 
print(str(x)) 

y  = (int (input("Enter number to be searched: ")))
print(str(y)) 

found = False

for index in x: 
    if index == y:
        found = True
        break
   
if found:
    print("Found")
else:
    print("Not Found")
       
       
    