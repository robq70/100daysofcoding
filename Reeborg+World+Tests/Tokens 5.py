def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    while object_here("token"):
        take("token")
    move()    
    if at_goal():
        done()
    if not object_here("token"):
        while carries_object("token"):
            put()
        move()    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
