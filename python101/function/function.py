#Simple Function
def print_function():
    print("Hello World! from python function")
    
print_function()


#Parameter Function
def param_function(param):
    print("Printing from Python parameter function")
    print(param+2)
    
param_function(8)

#Multiple Parameter Function

first_str="The number "

def function_mult_params(p1, p2, p3):
    print(p1+str(p2)+p3)


function_mult_params(first_str, 5, " is an integer.")


#Function with return parameters

def sum_func(p1 , p2):
    return p1+p2

sum = sum_func(5,2)
print ("Sum of parameters: ", sum)