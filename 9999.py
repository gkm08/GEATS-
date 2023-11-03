from cs1robots import*

load_world("worlds/newspaper.wld")
hubo = Robot(beepers=1)
hubo.set_trace('blue')
hubo.set_pause(0.1)


def turn_right():
    for i in range(3):
        hubo.turn_left()

for i in range(4):
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()


hubo.move()
hubo.drop_beeper()
hubo.turn_left()
hubo.turn_left()
hubo.move()



for i in range(4):
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()




