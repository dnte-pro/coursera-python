# addition
print(44 + 83)

# subtraction
print(83 - 44)

#divisiom
print(35 / 5)

# multiplication
print(5 * 5)

# modulus
print(10 % 3)

# exponentiation
print(2 ** 3)

# floor division
print(10 // 3)

# operator precedence
print(10 + 3 * 2)  # multiplication first   
print((10 + 3) * 2) # parentheses first
print(10 + 3 * 2 ** 2) # exponentiation first, then multiplication, then addition
print((10 + 3) * 2 ** 2) # parentheses first, then exponentiation, then multiplication
print((10 + 3 * 2) ** 2) # parentheses first, then multiplication, then exponentiation
print(10 + 3 * 2 // 2 - 5) # multiplication and floor division first, then addition, then subtraction
print((10 + 3) * 2 // (2 - 5)) # parentheses first, then multiplication, then floor division
print(10 + 3 * (2 // (2 - 5))) # parentheses first, then floor division, then multiplication, then addition
print(10 + 3 * 2 // (2 - 5) ** 2) # exponentiation first, then floor division, then multiplication, then addition
print((10 + 3 * 2) // (2 - 5) ** 2) # exponentiation first, then multiplication, then floor division, then parentheses


# logical operators
a = True
b = True

if a and b :
    print("All True! ")
else:
    print("Atleast one is false! ")

if a or b:
    print("At least one is true! ")
else:
    print("Both are false!")

if not(a) or not(b):
    print("All true!")
else: 
    print("Atleast one is false!")