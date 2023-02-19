example1 = [1, 2, 3]
example2 = ["green", "yellow", "blue"]
example3 = [1.14, 3.124, 5.678]
example4 = [1, True, "hello", 3.14]


print("Printing various types of list..")

print("Integer List:" + str(example1))
print("String List:" + str(example2))
print("Float List:" + str(example3))
print("Hetergeneous Data Types List:" + str(example4))


print("in example " + str(1 in example1))
print("not in example " + str(8 in example1))

print(list("blah"))