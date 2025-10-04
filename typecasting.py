#Typecasting is the process of converting a variable from one data type to another data type.
#python has two different types of typecasting: Implicit and explicit typecasting
"""Implicit typecasting is automatically done by the python interpreter without any user involvement"""
""""Explicit typecasting is done by the user to convert one data type to another data type using predefined functions like int(), float(), str(), etc."""

print(10 == 10.00)
print(10 + 10.00)
print(type(10 + 10.00))




userNum = input("Please enter the first number: ")
userNum2 = input("Please enter the second number: ")
userSum = float (userNum) + float (userNum2)
print("The sum of: " + userNum + "and " + userNum2 + " is " + str(userSum))