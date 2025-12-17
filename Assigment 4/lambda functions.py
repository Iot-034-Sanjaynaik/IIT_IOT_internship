# Lambda functions for conversions
km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
ft_to_in = lambda ft: ft * 12
in_to_cm = lambda inch: inch * 2.54

# General distance converter function
def distance_converter(distance, conversion_type, conversion_function):
    result = conversion_function(distance)
    print(f"{distance} {conversion_type.split(' to ')[0]} = {result} {conversion_type.split(' to ')[1]}")

# Input from user
distance = float(input("Enter distance: "))

# Perform all conversions
distance_converter(distance, "km to m", km_to_m)
distance_converter(distance, "m to cm", m_to_cm)
distance_converter(distance, "cm to mm", cm_to_mm)
distance_converter(distance, "ft to in", ft_to_in)
distance_converter(distance, "in to cm", in_to_cm)
