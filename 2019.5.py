from cs1robots import*

create_world()
hubo = Robot(beepers=100)
hubo.set_trace('blue')
hubo.set_pause(0.3)

hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
    hubo.move()

    if not hubo.front_is_clear():
        hubo.turn_left()
