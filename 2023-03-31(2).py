from cs1robots import*

load_world("worlds/trash1.wld")
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()



while not hubo.right_is_clear():
    if hubo.on_beeper():

        while hubo.on_beeper():
             hubo.pick_beeper()

    elif hubo.front_is_clear():
            hubo.move()

    else:
        hubo.turn_left()
        hubo.turn_left()

turn_right()
hubo.move()
while hubo.carries_beepers():
    hubo.drop_beeper()

