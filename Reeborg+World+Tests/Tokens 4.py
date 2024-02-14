def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    take("token")
    move()    
    if not object_here("token"):
        while carries_object("token"):
            put()
        move()    
    if at_goal():
        done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
