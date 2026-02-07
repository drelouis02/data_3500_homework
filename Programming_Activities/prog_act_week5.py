# ---------------------------------------------------------
# Activity 1
user_input = input("Enter a 3 digit number: ")
number = int(user_input)

# Get first digit using floor division
first_digit = number // 100

# Get third digit using modulus
third_digit = number % 10

# Check if digits match
if first_digit == third_digit:
    print("palindrome!!!!")
else:
    print("not palindrome!")



# ---------------------------------------------------------
# Activity 2
denominator = 2
total_sum = 0

for i in range(1, 1001):
    total_sum += 1 / denominator
    denominator *= 2  # Double denominator each time

print("The result of the series after 1000 terms is:", total_sum)



# ---------------------------------------------------------
# Activity 3
age = int(input("Enter child's age: "))
weight = float(input("Enter child's weight in pounds: "))

# Boolean conditions
age_12_or_older = age >= 12
age_11_and_90 = age == 11 and weight > 90
under_11_and_100 = age < 11 and weight > 100

# Decision
if age_12_or_older or age_11_and_90 or under_11_and_100:
    print("The child may sit in the front seat.")
else:
    print("The child may NOT sit in the front seat.")
