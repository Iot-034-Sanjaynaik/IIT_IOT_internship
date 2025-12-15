 # Function to check prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to print prime numbers in a range
def print_primes(start, end):
    print("Prime numbers in the given range:")
    for n in range(start, end + 1):
        if is_prime(n):
            print(n, end=" ")

# Input from user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

# Function call
print_primes(start,end)