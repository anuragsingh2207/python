
def factorial_calculate(fac_num):
    factorial =1 
    for i in range(1, fac_num+1):
        factorial = factorial * i
    return factorial    

print("Factorial of 3 is " + str(factorial_calculate(3)))
print("Factorial of 3 is " + str(factorial_calculate(4)))
print("Factorial of 3 is " + str(factorial_calculate(7)))