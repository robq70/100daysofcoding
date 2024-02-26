def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def take_leaf(a,b):
    for numbers in range(a,b):
        while object_here("leaf"):
            take()
        if wall_in_front() and wall_on_right():
            while carries_object():
                toss()
                if not carries_object("leaf"):
                    turn_left()
                    move()
                    turn_right()
                    move()
                    move()
                    turn_right()
                    move()
                    done()

        move()
take_leaf(0,5)
turn_left()
for numbers in range(0,3):    
    while is_facing_north() and front_is_clear():
        take_leaf(0,5)
        if wall_in_front():
            while object_here("leaf"):
                take()
            turn_left()
            move()
            turn_left()
    while not is_facing_north() and front_is_clear():
        take_leaf(0,5)
        if wall_in_front():
            while object_here("leaf"):
                take()
            turn_right()
            move()
            turn_right()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
