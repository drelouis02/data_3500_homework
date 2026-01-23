"""
Programming Activities - Completion Grade
"""

# -------------------------
# Programming Activity 1
# -------------------------
apple_price = 1.5          
number_purchased = 6       
tax = 1.07

total_bill = apple_price * number_purchased * tax

if total_bill == 0:
    print("Total bill is 0. Check your inputs (apple_price / number_purchased).")
else:
    print(f"Apples purchased: {number_purchased}")
    print(f"Total bill (with tax): ${total_bill:.2f}")

print()  


# -------------------------
# Programming Activity 2
# -------------------------
age_now = int(input("How old are you? "))
age_goal = int(input("What age would you like to live to? "))

years_left = age_goal - age_now

if years_left < 0:
    print("That goal age is younger than your current age — check your inputs.")
elif years_left == 0:
    print("You picked your current age — so approximately 0 years left by that goal.")
else:
    print(f"You have about {years_left} years left to live if you live to {age_goal}. Make them count 🙂")

print()


# -------------------------
# Programming Activity 3
# -------------------------
score = float(input("What is your score in this class (as a percent, e.g., 90 or 95)? "))

if score >= 93:
    print("Congratulations you got an A")
else:
    print("Congratulations, you still learned a ton!!!!")

print()



