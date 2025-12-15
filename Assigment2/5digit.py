# Accept a 5-digit number
num = int(input("Enter a 5-digit number: "))

# Store original number
original = num
reverse = 0

# Reverse the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check palindrome
if original == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")