#Valo Mara
#vmara2
#Monday 3:00PM
#Drawing concentric shapes

def drawSquare(turtle,size):
  forward(turtle,size)
  turnRight(turtle)
  forward(turtle,size)
  turnRight(turtle)
  forward(turtle,size)
  turnRight(turtle)
  forward(turtle,size)

def drawConcentricSquare(turtle):
  numSquare = 1
  
  while (numSquare < 20):
    drawSquare(turtle,numSquare*10)
    penUp(turtle)
    forward(turtle, 5)
    turnLeft(turtle)
    forward(turtle,5)
    turnRight(turtle)
    turnRight(turtle)
    penDown(turtle)
    numSquare = numSquare + 1

def writePic(picture):
  svFile = pickAFile()
  writePictureTo(picture,svFile)
  
pic = makeEmptyPicture(500,500)
t = makeTurtle(pic)

t.setPenWidth(1)
drawConcentricSquare(t)

writePic(pic)