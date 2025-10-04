num = input("Please enter the first number: ")
num2 = input ("Please enter the second number: ")
print(" You entered " + num + " and "  + num2 )
      
print(type(num))      
print(int(num) + int(num2))


str1 = input("What is your first name? ")
str2 = input("What is your last name? ")
print("Hello " + str1 + " " + str2)
print("Hello {} {}".format(str1, str2))
print(f"Your name is {str1} {str2}")