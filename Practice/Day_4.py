########################### CODE CHALLENGE ##################################
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#Write your code below this row 👇
horizontal = int(position[0])-1
vertical = int(position[1])-1

map[vertical][horizontal] = "X"

#Write your code above this row 👆
print(f"{row1}\n{row2}\n{row3}")


# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
print(names)
name = random.randint(0,(len(names)-1))

print(f"{names[name]} is going to buy the meal today!")

########### Random Module ############
# What is a module: each module is resposnible for different functionalities of your program

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails"

import random
number = random.randint(0,1)

if number == 0:
    print(f"{number}: Tails")
else:
    print(f"{number}: Heads")




