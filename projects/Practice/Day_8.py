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
        print(f"{number} is not  a prime number.")         

#is_prime_number(73)

####################### Caesar ###########################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"

def encrypt (text, shift):
    cipher_text  = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The cipher text is: {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt (text, shift):
    cipher_text  = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The cipher text is: {cipher_text}")
  

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(text, shift) 
elif direction == "decode":
    decrypt(text, shift)

