from cs1robots import*

load_world("worlds/hurdles1.wld")
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()


for i in range(4)   :
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()



hubo.move()
hubo.pick_beeper()

