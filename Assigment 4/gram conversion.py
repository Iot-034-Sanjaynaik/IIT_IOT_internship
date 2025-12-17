# List of lambda functions for conversions
conversions = [
    lambda t: t * 1000,                  # tonnes → kilograms
    lambda kg: kg * 1000,                 # kilograms → grams
    lambda g: g * 1000,                   # grams → milligrams
    lambda mg: mg / 453592.37              # milligrams → pounds
]

# Input from user
tonnes = float(input("Enter weight in tonnes: "))

# Apply conversions step by step
kg = conversions[0](tonnes)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

# Output
print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")
