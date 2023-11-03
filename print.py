from cs1robots import*

create_world()
hubo = Robot()
hubo.set_trace('blue')

def right():
    for i in range(4):
         hubo.turn_left(1)

right()
