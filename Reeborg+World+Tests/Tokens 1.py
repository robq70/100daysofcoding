def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
move()
take("token")
move()
put("token")
move()
if at_goal():
    done()
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
