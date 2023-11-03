from cs1robots import*

load_world("worlds/beepers3.wld")
hubo = Robot(beepers=100)
hubo.set_trace('blue')
hubo.set_pause(0.1)

for i in range(9):
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()
