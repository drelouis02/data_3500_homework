# ---------------------------------------------------------
# Problem 3.4
for row in range(2):          
    for col in range(7):      
        print('@', end='')    
    print()                   



# ---------------------------------------------------------
# Problem 3.9
num_str = input("Enter a number 7 to 10 digits: ")

if num_str.isdigit() and 7 <= len(num_str) <= 10:
    number = int(num_str)

    divisor = 10 ** (len(num_str) - 1)  

    while divisor > 0:
        digit = number // divisor      
        print(digit)
        number = number % divisor       
        divisor = divisor // 10         
else:
    print("Invalid input. Please enter a 7 to 10 digit integer.")




# ---------------------------------------------------------
# Problem 3.11
# This program repeatedly asks for gallons used and miles driven.
total_miles = 0
total_gallons = 0

while True:
    gallons = float(input("Enter the gallons used (-1 to end): "))

    if gallons == -1:
        break

    miles = float(input("Enter the miles driven: "))

    mpg = miles / gallons
    print(f"The miles/gallon for this tank was {mpg:.5f}")

    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    print(f"The overall average miles/gallon was {overall_mpg:.5f}")
else:
    print("No data entered.")


# ---------------------------------------------------------
# Problem 3.12
num_str = input("Enter a number: ")

reverse_str = ""
index = len(num_str) - 1

while index >= 0:
    reverse_str += num_str[index]
    index -= 1

if num_str == reverse_str:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


# ---------------------------------------------------------
# Problem 3.14
pi = 0
denominator = 1
sign = 1

count_314 = 0
count_3141 = 0

for i in range(1, 3001):
    pi += sign * (4 / denominator)
    denominator += 2
    sign *= -1

    pi_str = f"{pi:.5f}"

    if pi_str.startswith("3.14"):
        count_314 += 1
        if count_314 == 2:
            print(f"3.14 appeared twice in a row at iteration {i}")
    else:
        count_314 = 0

    if pi_str.startswith("3.141"):
        count_3141 += 1
        if count_3141 == 2:
            print(f"3.141 appeared twice in a row at iteration {i}")
    else:
        count_3141 = 0

