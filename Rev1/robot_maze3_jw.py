#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#------ change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#----- begin robot movement here
#   ------maze1 solution
'''
for step in range(4):
  move()
for turn in range(3):
  turn_left()
for step in range(4):
  move()
'''
#   -----maze2 solution1
'''
for step in range(3):
  move()
for turn in range(3):
  turn_left()
for step in range(2):
  move()
'''
#   -----maze2 solution2
'''
for turn in range(3):
  turn_left()
for sequence in range(2):
  for step in range(3):
    move()
  turn_left()
move()
'''
#   -----maze3 solution
'''
for sequence in range(4):
  move()
  for turn in range(3):
    turn_left()
  if sequence == 2:
    robot.pencolor("chartreuse1")
  move()
  turn_left()
'''
#---- end robot movement 

wn.mainloop()
