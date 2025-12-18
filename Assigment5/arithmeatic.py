
import sys

# Create the package
operations = types.ModuleType("operations")

# Create arithmetic module
arithmetic = types.ModuleType("arithmetic")
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
arithmetic.add = add
arithmetic.multiply = multiply

# Create string_ops module
string_ops = types.ModuleType("string_ops")
def reverse_string(s):
    return s[::-1]
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for c in s if c in vowels)
string_ops.reverse_string = reverse_string
string_ops.count_vowels = count_vowels

# Add modules to the package
operations.arithmetic = arithmetic
operations.string_ops = string_ops

# Register modules so they can be imported normally
sys.modules["operations"] = operations
sys.modules["operations.arithmetic"] = arithmetic
sys.modules["operations.string_ops"] = string_ops

# -----------------------------
# Demonstration Program
# -----------------------------
from operations.arithmetic import add, multiply
from operations.string_ops import reverse_string, count_vowels

print("Addition:", add(10, 5))
print("Multiplication:", multiply(10, 5))

text = "Hello World"
print("Reversed String:", reverse_string(text))
print("Vowel Count:", count_vowels(text))
