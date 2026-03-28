print("=== Programming Activities ===\n")

# Programming Activity 1
favorite_colors = ["blue", "white", "red"]
message = "My favorite colors are: "
colors_string = ", ".join(favorite_colors)
print(message + colors_string)

print("\n" + "="*30 + "\n")

# Programming Activity 2
address = input("Enter your address: ")
address_no_space = address.replace(" ", "")

if address_no_space.isalnum():
    print("Valid address!")
else:
    print("Invalid address! The address should only contain letters and numbers.")
