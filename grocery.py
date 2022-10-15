'''
A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:

Penne 16 oz Pack of 12 - $16.68

Arrabiata Pasta Sauce 24 oz - $6.98

Bag of 20 Organic Garlic Cloves - $16.78

Italian Seasoning 1.5 oz Bottle - $15.26

Artisan Baguettes Twin Pack - $3.00

12 oz Bag of Meatballs - $4.39

In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  The subtotal is just the sum of all of their prices.

Use print() to display the result of the expression.

'''



print("Please find below list of items purchased along with rate & quatity:") 
print("Penne 16 oz Pack of 12 - $16.68")  
print("Arrabiata Pasta Sauce 24 oz - $6.98")
print("Bag of 20 Organic Garlic Cloves - $16.78")
print("Italian Seasoning 1.5 oz Bottle - $15.26")
print("Artisan Baguettes Twin Pack - $3.00")
print("12 oz Bag of Meatballs - $4.39")
      
print("Calculating subtotal via round()")
total_round  = 16.68+6.98+16.78+15.26+3.00+4.39

print("Total Sum: $",round(total_round, 2))

penne = 16.68*100
pasta = 6.98*100
garlic = 16.78*100
seasoning = 15.26*100
baugettes = 3.00*100
meatballs = 4.39*100

print("Calculating subtotal via Multiply by 100")
total_int = (penne+pasta+garlic+seasoning+baugettes+meatballs)/100



print("Total Sum: $",total_int)





