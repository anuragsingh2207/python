score = int(input("Enter the score:"))

if score >= 90:
    print(" Grade A")
else:  
    if score >= 80 and score <= 90:
        print("Grade B")
    else:
        if score >= 70 and score <= 80:
              print("Grade C")    
        else: 
            if score >= 60 and score <= 70:
                print("Grade D")

            else:
                print("Grade F")    