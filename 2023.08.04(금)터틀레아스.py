import turtle as t
import winsound
import time
import random



t.bgcolor("lavender")
t.up()
t.speed(0)
t.goto(0, 220)
t.write("터틀 레이스", False, "center", ("",35))

t.goto(-400, 170)
t.down()
t.color("lightPink")
t.begin_fill()


for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()

t.color("black")
t.up()
t.goto(330, 200)
t.down()
t.goto(330, -250)



start_ycor = [150, 90, 30, -30, -90, -150, -210]
color_list = ["hotpink", "white", "red", "green", "yellow", "purple", "blue"]
turtles = []
for i in range(7):
    new_turtle = t.Turtle()
    new_turtle.up()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[i])
    new_turtle.goto(-350,start_ycor[i])
    new_turtle.write(i)
    new_turtle.goto(-350,start_ycor[i])
    turtles.append(new_turtle)


for i in range(6):
    t.up()
    t.goto(-400, start_ycor[i]-30)
    t.color("white")
    t.down()
    t.goto(400, start_ycor[i]-30)

user_choice = int(t.textinput("터틀레이스", "몇 번 거북이가 이길까요?"))
t.up()
t.goto(0,-200)
t.color("black")
t.write(f"{user_choice}번 터틀에 배팅하"
        f"셨습니다.", False, "center",("",30))


winsound.Beep(523, 300)
time.sleep(0.3)

game_over = False
while not game_over:
    for i in turtles:
        rand_speed = random.randint(1,10)
        i.forward(rand_speed)
        if i.xcor() > 330:
            game_over = True

#1등 찾기
max_xcor = 0
winner = 0
for i in range(len(turtles)):
    if turtles[i].xcor() > max_xcor:
        max_xcor = turtles[i].xcor()
        winner = i

t.goto(0,0)
if user_choice == winner:
    t.write("성공!", False, "center", ("",30))
else:
    t.write(f"실패! {winner}번 승", False, "center",("",30))

t.mainloop()


class whatisyourmajor(object):
  def __init__(self, name, school, major):
    self.name = name()
    self.school = school()
    self.major = major()


steve = whatisyourmajor('steve', 'abs', 'computer')