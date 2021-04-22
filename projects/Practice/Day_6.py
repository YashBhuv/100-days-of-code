def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    turn_left()
    turn_left()
    
def jump():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

path = [1,2,3,4,5,6]

for x in path:
    jump()



#################### EXERCISE 3 #####################
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    turn_left()
    turn_left()
    
def jump():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

path = [1,2,3,4,5,6]

while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()


################################## HURDLE 4 ############################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    turn_left()
    turn_left()
    
def jump():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def height():
    turn_left()
    move()
    
path = [1,2,3,4,5,6]

while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()
        height()
##############################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    turn_left()
    turn_left()
      
def jump():
    turn_left()
    
    while wall_on_right():
        move()
    
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    
    turn_left()    


while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        jump()