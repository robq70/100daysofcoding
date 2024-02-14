def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_stright():
    turn_left()
    move()
    turn_right()
    move()
    move()
def move_down():    
    move()
    move()
    turn_left()
    move()
    turn_right()
while True:
    take("star")
    for number in range (0,3):
        move_stright()
    put("star")
    if object_here("token"):
        take("token")
        if object_here("token"):
            take("token")
            if object_here("token"):
                take("token")
    turn_back()
    for number in range (0,3):
        move_down()
    done()

        
#if at_goal():       
#    done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
