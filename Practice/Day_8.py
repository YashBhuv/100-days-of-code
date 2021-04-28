###################################################### Exercise 1 ###############################################
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
import math
def greet():
    print("Hello World!")
    print("You are strong and beautiful")
    print("Believe in yourself!")

#greet()

# Function that allows for an Input 

def greet_with_name(name):
    print(f"Hello {name}!")

#greet_with_name("Yashitha")

################ FUNCTION WITH MULTIPLE INPUTS
# POSITIONAL ARGUEMENT IS IMPORTANT
def greet_with(name, location):
    print(f"Hello {name}, aren't yor from {location}")

#greet_with("Yashitha", "Toronto")
    # Positional arguement example is shown below:
#greet_with(location = "Toronto", name = "Yashitha")

################### CODE CHALLENGE ######################

def cans_of_paint(height, width):
    num_cans = math.ceil((height * width) / 5)
    print(f"You will require {num_cans} of paint.")

#cans_of_paint(3, 9)

###################### Prime number check ####################
#Prime numbers are numbers that can only be cleanly divided by itself and 1.

def is_prime_number(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number.") 
    else:
        print(f"{number} is not a prime number.")         

is_prime_number(73)





