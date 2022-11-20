from operator import length_hint


def rectangle_voulme(l, b,h):
    return l*b*h


print ("Calculate Volume of Rectangle")
length = int(input("Enter lenght of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
height = int(input ("Enter height of rectangle: "))

volume = rectangle_voulme(length, breadth, height)
print ("Volume of Rectangle: ", volume)
