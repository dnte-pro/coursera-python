bill_total = 95

bill_discount = 10 

if bill_total > 100:
    print("Total bill is greater than 100")
    bill_total = bill_total - bill_discount

print("Total bill after discount is " + str(bill_total))
