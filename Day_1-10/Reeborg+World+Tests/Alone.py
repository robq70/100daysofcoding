def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
for number in range(0,5):
    for number in range(0,10):
        if front_is_clear():
            move()
            if wall_in_front():
                turn_left()
                move()
                turn_left()
        if front_is_clear():
            move()
            if wall_in_front():
                if wall_in_front() and wall_on_right():
                    done()
                    
                turn_right()
                move()
                turn_right()
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
