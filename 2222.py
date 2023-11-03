from cs1robots import*

load_world("worlds/harvest1.wld")
hubo = Robot(beepers=1)
hubo.set_trace('blue')
hubo.set_pause(0.1)
def turn_right():
     for i in range(3):
          hubo.turn_left()


def hubo_move():
     hubo.move()
     hubo.pick_beeper()


for i in range(4):
     hubo_move()
     hubo.turn_left()
     for i in range(5):
          hubo_move()
     turn_right()
     hubo_move()
     turn_right()
     for i in range(5):
          hubo_move()
     hubo.turn_left()



