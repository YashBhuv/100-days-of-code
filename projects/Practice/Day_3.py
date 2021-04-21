########### Exercise 7 ############################################
# You are going to write a program that tests the compatibility between two people.
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculasarator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Write your code below this line 👇
name_a = name1.lower() + name2.lower()
numb1 = 0
numb1 += name_a.count('t')
numb1 += name_a.count('r')
numb1 += name_a.count('u')
numb1 += name_a.count('e')

numb2 = 0
numb2 += name_a.count('l')
numb2 += name_a.count('0')
numb2 += name_a.count('v')
numb2 += name_a.count('e')

number = str(numb1) + str(numb2)
new_num = int(number)

if new_num < 10 or new_num > 90:
    print(f"Your score is {new_num}. You go together like coke and mentos.")
elif new_num >= 40 and new_num <= 50:
    print(f"Your score is {new_num}, you are alright together.")
else:
    print(f"Your love score is {new_num}")

########### Exercise 6 #############################################
#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 
#Based on a user's order, work out their final bill. 
print("Welcome to Python Pizza")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == 'S':
    bill += 15
    print("A small pizza costs $15")

elif size == 'M':
    bill += 20
    print("A medium pizza costs $20")

else:
    bill += 25
    print("A large pizza costs $25")

if add_pepperoni == 'Y':
    if size == "S":
        bill += 2
    else:
            bill += 3
    
if extra_cheese == 'Y':
    bill += 1
    print(f"Your total comes to ${bill}")

########### Exercise 5############################################
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter your age? "))
    if age < 12:
       print("child tickets are $5.")
       bill = 5
    elif age <=18:
        print("youth tickets are $7.")
        bill = 7
    else:
        print("adult tickets are $12.")
        bill = 12

    photo = input("Do you want a photo take? Y or N: ")
    if photo == "Y":
        #Add $3 to bill
        print("A photo will cost $3")
        bill += 3
       
    print(f"Your total is ${bill}.")
else:
    print("Sorry, you have to grow taller before you ride.")

########### Exercise 4############################################

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, 
# with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Is a leap year")
        else:
            print("Is not a leap year")
    else:
        print("Is a leap year!")
else:
    print("Is not a leap year!")

########### Exercise 3############################################
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
weight = float(input("Please enter your weight in kg? "))
height = float(input("Please enter your height in m? "))

bmi = round(weight/(height**2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are under weight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are at normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


########### Exercise 2############################################
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you ride.")

############ Exercise 1###########################################
# Write a program that works out whether if a given number is an odd or even number

num = int(input("Please type a number? "))

if num % 2 == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")


############ Practicing ifs and elifs##############################
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you ride.")
