from cs1robots import*

load_world("worlds/harvest3.wld")
hubo = Robot(beepers=100)
hubo.set_trace('blue')
hubo.set_pause(0.1)

def zero():
    hubo.move()
    if not hubo.on_beeper():
        hubo.drop_beeper()

def turn_right():
    for i in range(3):
        hubo.turn_left()

for i in range(3):

    for i in range(6):
        zero()

    hubo.turn_left()
    zero()
    hubo.turn_left()

    for i in range(6):
        zero()

    turn_right()
    zero()
    turn_right()


