input_str = input("Enter non-empty string: ")
char_count = 0


for letter in input_str:
    char_count += 1
    
print("Input String: " + input_str)
print("Character Count: " + str(char_count))