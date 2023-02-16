from tax import calculateTax


print()
print("Hellou")
print()
dates1 =float(input("Please print you amount - "))
##if dates1!=float or int: 
    #  print("TypeError. Please enter only a number. For example '200' or '150.40'")
    

dates2 =float(input("Please print procent - "))
dates3= 'amount'
rezult= calculateTax(dates1, dates2, dates3)
print("rezult-", rezult[3], rezult[2])
