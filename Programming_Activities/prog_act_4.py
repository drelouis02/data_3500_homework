# -------------------------------
# Programming Activity 1
# -------------------------------

birth_year = int(input("Enter the year you were born: "))

if birth_year >= 1997:
    print("You are a Zoomer")
elif birth_year >= 1981:
    print("You are a Millennial")
elif birth_year >= 1965:
    print("You are Gen X")
elif birth_year >= 1946:
    print("You are a Baby Boomer")
else:
    print("Generation not listed")


# -------------------------------
# Programming Activity 2
# -------------------------------

age = int(input("\nEnter your age: "))
current_year = 2025  # you can update this if needed

while age > 1:
    print("You were alive in year:", current_year)
    age -= 1
    current_year -= 1
else:
    print("You were born in year:", current_year)


# -------------------------------
# Programming Activity 3
# -------------------------------

print("\nMultiples of 5 using a for loop:")
for num in range(5, 100, 5):
    print(num)


# -------------------------------
# Programming Activity 4
# -------------------------------

print("\nMultiples of 5 using a while loop:")
num = 5
while num <= 95:
    print(num)
    num += 5

