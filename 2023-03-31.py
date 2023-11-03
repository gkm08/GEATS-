from cs1robots import*

load_world("worlds/hurdles3.wld")
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.001)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def jump():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

while not hubo.on_beeper():

    if hubo.right_is_clear():
        hubo.move()

    else:
        jump()