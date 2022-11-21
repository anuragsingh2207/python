def c_to_f(c):
    return 1.8*c + 32


print ("Celsius to Fahrenheit Conversion")

c = int(input("Enter temperature in Celsius: "))
f = c_to_f(c)
print ("Fahrenheit Converted temperature: ", f)
