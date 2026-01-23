#imports
import turtle as trtl

#global
#maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
startHeading = 90
turtle_scale = 1.5
mazeList = ["maze1.png","maze2.png","maze3.png"]

#functions
#robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turnLeft():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def checkForWin(winX,winY):
  if (robot.xcor() > winX-1 and robot.xcor() < winX+1) and (robot.ycor() > winY-1 and robot.ycor() < winY+1):
    for i in range(len(mazeList)):
      if mazeList[i] == wn.bgpic():
        robot.clear()
        robot.teleport(startx,starty)
        robot.setheading(startHeading)
        wn.bgpic(mazeList[(i+1)%len(mazeList)])
        break
  else:
    print("You have not won yet.")



#init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#initRobot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(startHeading)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()


#change maze here
wn.bgpic("maze1.png")

#mainloop
while True:
  #maze1 solution
  for step in range(4):
    move()
  for turn in range(3):
    turnLeft()
  for step in range(4):
    move()
  checkForWin(100,100)

  #maze2 solution1
  for step in range(3):
    move()
  for turn in range(3):
    turnLeft()
  for step in range(2):
    move()
  checkForWin(0,50)

  #maze2 solution2
  '''
  for turn in range(3):
    turnLeft()
  for sequence in range(2):
    for step in range(3):
      move()
    turnLeft()
  move()
  '''

  #maze3 solution
  for sequence in range(4):
    move()
    for turn in range(3):
      turnLeft()
    if sequence == 2:
      robot.pencolor("chartreuse1")
    move()
    turnLeft()
  checkForWin(100,100)

wn.mainloop() #keep screen running
