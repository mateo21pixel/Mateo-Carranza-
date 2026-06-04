# Take two input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Add them
result = num1 + num2

# Print the result
print("Result:", result)
 
# Which operation the user want
print ("Choose operation: +, -, *, /")
operation = input()
num1 = float(input("enter firs number: "))
num2 = float (input("enter second number: "))

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)

