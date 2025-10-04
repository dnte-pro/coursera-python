bill_total = 95

bill_discount = 10 

if bill_total > 100:
    print("Total bill is greater than 100")
    bill_total = bill_total - bill_discount
else:
    print("Bill is less than or equal to 100")

print("Total bill after discount is " + str(bill_total) + "\n")


# testing with bill greater than 100
print("Now testing with bill total greater than 100")
bill_total = 150

bill_discount = 10 

if bill_total > 100:
    print("Total bill is greater than 100")
    bill_total = bill_total - bill_discount

print("Total bill after discount is " + str(bill_total))



#nested if-else
print("\nNow testing with bill total greater than 200")
bill = 300 
discount1 = 10 
discount2 = 20 

if bill > 100 and bill <= 200:
    print("Bill is greater than 100")
    bill = bill - discount1

elif bill > 200:
    print("Bill is greater than 200")
    bill = bill - discount2

else:
    print("Bill is less than 100")

print("Bill after discount is "+ str(bill))



current = False

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')
