from karel.stanfordkarel import *

# MIDPOINT KAREL ‘RECURSION’

# Karel uses recursion to find the middle
# recursion function - moves 2 times (if no wall) and then calls recursion function
# then, being sure to face west, karel moves once ( for each time recursion was called)
# Karel is now in the middle
# put beeper and turn around to face east


def main():
    recursion_find_middle()
    put_beeper()
    turn_around()

def recursion_find_middle():
    if front_is_clear():
        move()
        safe_move()
        recursion_find_middle() # recursion start here
        while not_facing_west():
            turn_left()
        move()

def safe_move():
    if front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

# don't change this code
if __name__ == '__main__':
    main()
