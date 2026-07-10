# Type Casting in Python

age = "22"
height = "5.8"
number = 100

print("Before Type Casting")
print(age, type(age))
print(height, type(height))
print(number, type(number))

age = int(age)
height = float(height)
number = str(number)

print("\nAfter Type Casting")
print(age, type(age))
print(height, type(height))
print(number, type(number))