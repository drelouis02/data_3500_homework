def welcome_fctn(name):
    print("Welcome " + name)

# call the function
welcome_fctn("Andre")

def welcome_fctn2(name):
    welcome_message = "Welcome " + name
    return welcome_message

# test option 1
print(welcome_fctn2("Bob"))

# test option 2
message = welcome_fctn2("Andre")
print(message)
def welcome_fctn3(name, age, favorite_color):
    welcome_message = "Welcome " + name + ", you are " + str(age) + " years old, and " + favorite_color + " is your favorite color"
    return welcome_message

# test the function
print(welcome_fctn3("Andre", 22, "green"))
