# Programming Activity 1
even_numbers = [num for num in range(2, 101) if num % 2 == 0]
print("Even numbers:", even_numbers)


# Programming Activity 2
strings = ["  hello  ", " world", "python  ", "  code"]
cleaned_strings = [s.strip() for s in strings]
print("Cleaned strings:", cleaned_strings)


# Programming Activity 3
name = input("Enter your name: ")
name_upper = name.upper()
print(f"welcome, {name_upper}!")


# Programming Activity 4
sentence = "dude, I just biked down that mountain and at first I was like Whoa, and then I was like Whoa"

# print original
print("\nOriginal sentence:")
print(sentence)

# capitalize first letter
sentence = sentence.capitalize()

# split into words
words = sentence.split()

# change first and second "Whoa"
count = 0
for i in range(len(words)):
    if words[i] == "Whoa,":
        if count == 0:
            words[i] = "whoa,"
        elif count == 1:
            words[i] = "WHOA"
        count += 1

# join back into sentence
sentence = " ".join(words)

# append exclamation
sentence += "!"

# print updated sentence
print("\nUpdated sentence:")
print(sentence)
