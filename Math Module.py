import math

num = float(input("Enter a number: "))

Square_root = math.sqrt(num)
Logarithm= math.log(num) if num > 0 else "Undefined (logarithm is only defined for positive numbers)"
Sine = math.sin(num)

print(f"Square root: {Square_root}")
print(f"Natural logarithm: {Logarithm}")
print(f"Sine (in radians): {Sine}")
