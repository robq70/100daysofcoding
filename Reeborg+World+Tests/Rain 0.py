def turn_back():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while True:
    for number in range(0,6):
        move()
    build_wall()
    turn_back()
    for number in range(0,5):
        move()
    done()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
