"""
HW2 - Variables, Math, Output
Problems: 2.3 through 2.8

Name: Andre Louis
"""

# -------------------------
# 2.3 (FILL IN THE MISSING CODE)

grade = 91 

if grade >= 90:
    print(f"Congratulations! Your grade of {grade} earns you an A in this course!")

print()  # spacer line so output is easier to read


# -------------------------
# 2.4 (ARITHMETIC)

left = 27.5
right = 2

print("2.4 Arithmetic with 27.5 and 2:")
print(left + right)
print(left - right)
print(left * right)
print(left / right)
print(left // right)
print(left ** right)

print()


# -------------------------
# 2.5 (CIRCLE AREA, DIAMETER AND CIRCUMFERENCE)

pi = 3.14159
r = 2

diameter = 2 * r
circumference = 2 * pi * r
area = pi * (r ** 2)

print("2.5 Circle with radius 2:")
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Area:", area)

print()


# -------------------------
# 2.6 (ODD OR EVEN)

number = 7  # change this to test

print("2.6 Odd or Even:")
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

print()


# -------------------------
# 2.7 (MULTIPLES)

print("2.7 Multiples:")

if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else:
    print("1024 is not a multiple of 4")

if 2 % 10 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")

print()


# -------------------------
# 2.8 (TABLE OF SQUARES AND CUBES)

print("2.8 Table of squares and cubes:")
print("number\tsquare\tcube")

for n in range(0, 6):
    print(f"{n}\t{n**2}\t{n**3}")
