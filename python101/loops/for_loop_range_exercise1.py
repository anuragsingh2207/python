number = range(1, 50)


for num in number:
    print(num)
    if num % 3 == 0 or num % 5 == 0:  
        print("FizzBizz")
    elif num % 3 == 0 :
        print("Fizz")
    elif num % 5 == 0 :
        print("Buzz")
    else :
        print("Neither Fizz nor Buzz")