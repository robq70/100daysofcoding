def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
    if object_here("token"):
        take("token")
        move()
        put("token")
    if at_goal():
        done()
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
