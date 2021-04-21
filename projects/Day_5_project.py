##Password Generator Project
import random
from random import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1,nr_letters + 1):
    random_char =random.choice(letters)
    password = password + random_char

for symb in range(1, nr_symbols +1):
    random_symb = random.choice(symbols)
    password = password + random_symb

for numb in range(1, nr_numbers + 1):
    random_numb = random.choice(numbers)
    password = password + random_numb

print(f"Your generated password: {password}")

# Shuffle the letter in generated password:
pass_rand = password
shuffled = list(pass_rand)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print("Your randmoized password is: ")
print(shuffled)

