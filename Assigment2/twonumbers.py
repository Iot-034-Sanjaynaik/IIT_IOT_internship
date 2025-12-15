# Accept two numbers from the user
num1 = float(input("Enter the first number (Dividend): "))
num2 = float(input("Enter the second number (Divisor): "))

# Check for divide by zero
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print("Division result=",result)