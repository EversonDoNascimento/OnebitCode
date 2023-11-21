number1 = float(input("Type it the first number: "))
number2 = float(input("Type it the second number: "))
operation = input("Type it the operations: (+, -, /, *)  ")

if(operation== '+'):
    print(f"The result of sum of numbers is: {number1 + number2}")

elif(operation == "-"):
    print(f"The result of subtration of numbers is: {number1 - number2}")
    
elif(operation == "/"):
    print(f"The result of division of numbers is: {number1 / number2}")

elif(operation == "*"):
    print(f"The result of multiplication of numbers is: {number1 * number2}")

else:
     print(f"Invalid operation!")

