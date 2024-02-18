def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
move()
move()
move()
turn_right()
move()
while True:
    if front_is_clear():
        move()
    else:
        turn_left()
    if at_goal():
        turn_right()
        done()
    if not wall_on_right():
        move()
        if front_is_clear() and right_is_clear():
            turn_back()
            move()
            turn_left()
            move()
        elif front_is_clear() or wall_in_front() and wall_on_right():
            turn_back()
            move()
            turn_left()
            build_wall()
            turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
