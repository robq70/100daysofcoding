def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while True:
    if front_is_clear():
        move()
        if front_is_clear():
            move()
            if front_is_clear():
                move()
    if wall_in_front() and right_is_clear():
        turn_right()
    if front_is_clear() and right_is_clear():
        turn_right()
        if front_is_clear() and is_facing_north():
            move()
        else:
            turn_left()
            move()    
    if front_is_clear() and is_facing_north():
        move()
        if front_is_clear():
            move()
    if wall_on_right()and wall_in_front():
        turn_left()
        if front_is_clear():
            move()
            if front_is_clear():
                move()
                if wall_on_right() and front_is_clear():
                    turn_left()
                    if front_is_clear():
                        move()
                        
    if at_goal():       
        done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
