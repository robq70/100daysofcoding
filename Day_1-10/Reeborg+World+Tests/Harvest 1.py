def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_left()
while True:    
    if object_here():
        take()
        move()            
    elif is_facing_north():
            move()
            if wall_in_front():
                turn_right()
                move()
                turn_right()

    elif not is_facing_north():
            move()
            if wall_in_front():
                turn_left()                
                if wall_in_front():                
                    done()
                move()    
                turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
