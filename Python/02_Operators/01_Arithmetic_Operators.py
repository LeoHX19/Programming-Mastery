# Program: Arithmetic Operators in Python

# Taking user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n===== Arithmetic Operators =====")

# Addition
print(f"{num1} + {num2} = {num1 + num2}")

# Subtraction
print(f"{num1} - {num2} = {num1 - num2}")

# Multiplication
print(f"{num1} * {num2} = {num1 * num2}")

# Division
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Division: Cannot divide by zero.")

# Floor Division
if num2 != 0:
    print(f"{num1} // {num2} = {num1 // num2}")
else:
    print("Floor Division: Cannot divide by zero.")

# Modulus (Remainder)
if num2 != 0:
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Modulus: Cannot divide by zero.")

# Exponentiation (Power)
print(f"{num1} ** {num2} = {num1 ** num2}")