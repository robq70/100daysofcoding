def put_move():
        put()
        move()
def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def ref_object():
    take()
    turn_back()
    move()
while True:
    if front_is_clear() and wall_on_right():
        # OK dla duzego
        put_move()
        while True:
            if object_here():
                ref_object()
                put_move()
                if object_here() and is_facing_north():
                    ref_object()
                    done()
                if object_here():
                    ref_object()
                    if object_here() and not wall_on_right():
                        take()
                        turn_right()
                        put()
                        move()
                    if object_here() and wall_on_right():                        
                        done()
            elif front_is_clear():
                move()
            elif wall_in_front() and object_here():
                ref_object()
                put()
            elif wall_in_front():
                turn_back()
                put_move()
    if wall_in_front():        
        # pionowe ok
        turn_left()
        put()
        if wall_in_front():
            put()
            turn_left()
            take()
            done()
        move()
        while True:
            if object_here():
                ref_object()
                put_move()
                if object_here():
                    ref_object()
                    done()
            elif front_is_clear():
                move()
            elif wall_in_front() and object_here():
                ref_object()
                put()
            elif wall_in_front():
                turn_back()
                put_move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
