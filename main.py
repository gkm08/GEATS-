from cs1robots import*

create_world()
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(9):
        hubo.turn_left()

def move9():
    for i in range(9):
        hubo.move()

for i in range(4):
    move9()
    hubo.turn_left()




