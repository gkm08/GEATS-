from cs1robots import*

load_world("worlds/amazing3.wld")
hubo = Robot(beepers=100)
hubo.set_trace('blue')
hubo.set_pause(0.1)


def turn_right():
    for i in range(3):
        hubo.turn_left()


hubo.drop_beeper()
if  not hubo.front_is_clear():
    hubo.turn_left()
hubo.move()
while not hubo.on_beeper():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
