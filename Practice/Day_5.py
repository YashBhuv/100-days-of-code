########################################### EXERCISE 5 #############################################################
# Write a program for the FizzBuzz Game

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

########################################### EXERCISE 4 #############################################################
# Calculate the sum of even numbers from 1-100
total = 0
for number in range(0,101,2):
    total += number
print(total)

########################################### EXERCISE 3 #############################################################
# addind all the numbers from 1 - 100
total = 0
for x in range(1,101):
    total += x
print(total)
########################################### EXERCISE 2 #############################################################
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

current_max = student_scores[0]
for x in student_scores:
   if x > current_max:
      current_max = x
print(f"The highest score in the class is: {current_max}")

current_low = student_scores[0]
for y in student_scores:
    if y < current_low:
        current_low = y
print(f"The lowest grade in the class is: {current_low}")
        

########################################### FOR LOOPS PRACTICE #####################################################
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

len = 0
total = 0

for length in student_heights:
    len += student_heights.count(length)
print(f"There are {len} elements in the list.")

for totals in student_heights:
    total += totals
print(f"The sum of all heaights is: {total}.")

avg = round(total / len)
print(f"The average height is: {avg}.")
    
  