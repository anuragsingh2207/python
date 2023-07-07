x, y = input("Enter two values: ").split()

l = int(x)
r = int(y)

 
def find_odd(l, r):
    if l<1:
        print("Start range less than 1")
    elif r<l:
        print("End range smaller than Start range")
    elif l>10**5:
        print("End range larger than 10^5")
    else: 
        for num in range(l,r+1):
            if num %2 != 0:            
                print(num)
   
                
                
find_odd(l, r)
                
                
       
                  
        
        
    