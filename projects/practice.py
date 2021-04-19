
#Print the number of characters in the input name

#Method 1, calling a variable 
name = input("What is your name?")
print(len(name))
#Method 2, nesting code 
print(len(input("What is your name?")))

#Switch the variables 

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c

#Write your code above this line 👆1
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)