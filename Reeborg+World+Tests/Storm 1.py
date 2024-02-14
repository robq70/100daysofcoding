def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while True:
    for numbers in range (0,5):
        move()
        while object_here("leaf"):
            take()
    turn_back()
    for numbers in range (0,5):
        move()
    turn_right()
    while carries_object():
        toss()   
    if at_goal():
        done()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
