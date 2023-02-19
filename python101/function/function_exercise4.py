import random



print("Calculate Miles per Gallon\n")

gallons = random.randint(10, 25)
print ("Gallons: "+str(gallons))

miles = random.randint(200, 400 )
print("Miles: "+str(miles))


miles_per_gallon = miles//gallons

print("Miles per Gallon: "+str(miles_per_gallon))
