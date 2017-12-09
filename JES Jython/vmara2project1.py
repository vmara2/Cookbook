#Valo Mara
#vmara2
#CS111 Lab Monday 3:00PM
#Drawing multifaceted shapes on pictures

    
def drawHexagon(turtle,size,color):
  turtle.setPenColor(color)
  sideCount = 1
  while (sideCount <= 6):
    forward(turtle,size)
    turn(turtle,360/6)
    sideCount = sideCount + 1

#drawMoon draws a hexagon moon with rectangle rays       
def drawMoon(turtle, size, color):
  rayCount = 1
  turtle.setPenColor(color)
  turtle.penUp()
  turtle.moveTo(1300,400)
  turtle.penDown()
  drawHexagon(turtle,size,color)
  turn(turtle,360/60)
  turtle.penUp()
  forward(turtle,size/2)
  turnLeft(turtle)
  forward(turtle,size/2)
  turtle.penDown()
  while (rayCount <= 6):
    drawRectangle(turtle,size/2,size/4,color)
    turtle.penUp()
    turnLeft(turtle)
    forward(turtle,size/2)
    turnLeft(turtle)
    forward(turtle,size/2)
    turn(turtle,360/6)
    forward(turtle,size/2)
    turnLeft(turtle)
    forward(turtle,size/2)
    turtle.penDown()
    rayCount = rayCount + 1
  
  
def drawRectangle(turtle,length,width,color):
  t2.setPenColor(color)
  forward(turtle,length)
  turnRight(turtle)
  forward(turtle,width)
  turnRight(turtle)
  forward(turtle,length)
  turnRight(turtle)
  forward(turtle, width)
  
def drawDiamond(turtle,size,color):
  sideCount = 1
  while (sideCount <= 2):
    turn(turtle,360/3)
    forward(turtle,size)
    turn(turtle,360/6)
    forward(turtle,size)
    sideCount = sideCount + 1

#drawFourStar uses four diamonds to draw a four point star        
def drawFourStar(turtle,size,color):
  shapeCount = 0
  while (shapeCount < 4):
    drawDiamond(turtle,size,color)
    turn(turtle,360/4)
    shapeCount = shapeCount + 1


#draws a regular five point star
def drawStar(turtle):
  sideCount = 0
  while (sideCount < 5):
    forward(turtle,25)
    turn(turtle, 720/5)
    sideCount = sideCount + 1
    turtle.setPenColor(yellow)

#drawConstellation uses five point stars to draw a terrible big dipper        
def drawConstellation(turtle,clr):
  turtle.setPenColor(clr)
  turtle.setPenWidth(5)
  penUp(turtle)
  moveTo(turtle,200,200)
  penDown(turtle)
  drawStar(turtle)
  turtle.setPenWidth(1)
  moveTo(turtle,325,201)
  turtle.setPenWidth(5)
  drawStar(turtle)
  turtle.setPenWidth(1)
  moveTo(turtle,425,300)
  turtle.setPenWidth(5)
  drawStar(turtle)
  turtle.setPenWidth(1)
  moveTo(turtle,525,400)
  turtle.setPenWidth(5)
  drawStar(turtle)
  turtle.setPenWidth(1)
  moveTo(turtle,530,550)
  turtle.setPenWidth(5)
  drawStar(turtle)
  turtle.setPenWidth(1)
  moveTo(turtle,800,650)
  turtle.setPenWidth(5)
  drawStar(turtle)
  turtle.setPenWidth(1)
  moveTo(turtle,850,450)
  turtle.setPenWidth(5)
  drawStar(turtle)
  turtle.setPenWidth(1)
  moveTo(turtle,525,400)
  
fname = pickAFile()
pic = makePicture(fname)
t1 = makeTurtle(pic)
t2 = makeTurtle(pic)

drawConstellation(t1, yellow)

drawMoon(t2,100,cyan)

t2.penUp()
t2.moveTo(900,200)
t2.penDown()
drawFourStar(t2,50,cyan)

pic.show()
