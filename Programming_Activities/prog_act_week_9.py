# Programming Activity 1
import os

name = input("Enter your name: ")
color = input("Enter your favorite color: ")

filename = "favorite_color.txt"

with open(filename, "w") as file:
    file.write(name + "'s favorite color is " + color)

os.startfile(filename)

# Programming Activity 2
import numpy as np

array = np.zeros(100)
array = np.random.random(100)

print(array)
