def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def take_leaf():
    while object_here("leaf"):
        take()
move()
take_leaf()
turn_left()
move()
take_leaf()
move()
take_leaf()
turn_left()
move()
take_leaf()
turn_right()
while True:    
    if not front_is_clear():
        turn_left()
        take_leaf()
        move()
        turn_right()
        take_leaf()
        move()
        take_leaf()
        move()
        take_leaf()
        turn_right()
        move()
        take_leaf()
        turn_left()
        if wall_in_front():
            turn_right()
            move()
            turn_right()
            
        
        
    while front_is_clear() and is_facing_north():
        take_leaf()
        move()
        if wall_in_front():
            take_leaf()
            turn_right()
            if wall_in_front():
                turn_right()
                while front_is_clear():
                    move()
                turn_right()
                while front_is_clear():
                    move()
                turn_right()
                while carries_object():
                    toss()
                done()
            move()            
            turn_right()
    while front_is_clear() and not is_facing_north():
        take_leaf()
        move()
        if wall_in_front():
            take_leaf()
            turn_left()
            if wall_in_front():
                turn_back()
                while front_is_clear():
                    move()
                turn_right()
                while carries_object():
                    toss()
                done()
                
                
                        
            move()            
            turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
