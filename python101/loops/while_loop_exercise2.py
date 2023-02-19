init_num = int(input("Eneter any non-negative number:"))
updt_num = init_num
sum = 0

while updt_num > 0:
      sum += updt_num
      updt_num -= 1
      
      
print("Input Number:" + str(init_num))
print("Sum:" + str(sum))
