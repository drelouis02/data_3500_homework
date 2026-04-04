import json

"""
Programming Activity 1
"""

# ask user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# create the 2D list
multiplication_table = []

for i in range(1, num1 + 1):
    row = []
    for j in range(1, num2 + 1):
        row.append(i * j)
    multiplication_table.append(row)

# print the table using another nested for loop
print("\nMultiplication Table:")
for row in multiplication_table:
    for value in row:
        print(value, end="\t")
    print()


"""
Programming Activity 2
"""

# ask user for age and favorite color
age = input("\nEnter your age: ")
favorite_color = input("Enter your favorite color: ")

# store values in dictionary
person_info = {
    "age": age,
    "favorite_color": favorite_color,
    "multiplication_table": multiplication_table
}

# print all values by iterating through the keys
print("\nDictionary Values:")
for key in person_info:
    print(person_info[key])


"""
Programming Activity 3
"""

# load person.json into a dictionary
with open("person.json", "r") as file:
    person = json.load(file)

# increase age by 1
person["age"] += 1

# save updated dictionary back to person.json
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# verify contents were updated
with open("person.json", "r") as file:
    updated_person = json.load(file)

print("\nUpdated person.json contents:")
print(updated_person)


"""
Programming Activity 4
"""

# ask user for two numbers
number1 = float(input("\nEnter a number to divide: "))
number2 = float(input("Enter a number to divide by: "))

try:
    result = number1 / number2
    print("Result:", result)
except ZeroDivisionError:
    print("Error, attempted to divide by zero")
