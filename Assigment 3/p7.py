# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:      # Base case
        return 1
    return n * factorial(n - 1)


# Recursive function to find power
def power(base, exp):
    if exp == 0:             # Base case
        return 1
    return base * power(base, exp - 1)


# Testing the functions
num = int(input("Enter a number for factorial: "))
print("Factorial of", num, "is:", factorial(num))

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Power result:", power(base,exp))