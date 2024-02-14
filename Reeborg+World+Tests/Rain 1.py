def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
move()
turn_right()
while True:
    if front_is_clear():
        move()
    else:
        turn_left()
    if at_goal():
        turn_right()
        done()
    if not wall_on_right():
        turn_right()
        build_wall()
        turn_left()

        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
