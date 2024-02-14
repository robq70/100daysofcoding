def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def farm_carrot():    
    if object_here():
        take()
        if object_here():
            take()
            if object_here():
                take()
    if not object_here():
        put()
        move()
move()
move()
turn_left()
move()
move()

for number1 in range (0,3):
    for number in range(0, 6):
        farm_carrot()

    turn_right()
    move()
    turn_right()
    move()

    for number in range(0, 6):
        farm_carrot()

    turn_left()
    move()
    turn_left()
    move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
