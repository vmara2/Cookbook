#Valo Mara
#vmara2
#Monday at 3PM
#Drawing initals with turtle

my_world = makeWorld()
ricardo = makeTurtle(my_world)

ricardo.setPenWidth(7)
ricardo.setPenColor(red)

#Draws the letter V
turn(ricardo,335)
forward(ricardo,111)
turn(ricardo,180)
forward(ricardo,111)
turn (ricardo,230)
forward(ricardo,111)

penUp(ricardo)
turn(ricardo,65)
forward(ricardo,25)

#Draws the letter M
ricardo.setPenColor(blue)
penDown(ricardo)
turnRight(ricardo)
forward(ricardo,100)
turn(ricardo,180)
forward(ricardo,100)
turnRight(ricardo)
forward(ricardo,50)
turnRight(ricardo)
forward(ricardo,100)
turn(ricardo,180)
forward(ricardo, 100)
turnRight(ricardo)
forward(ricardo, 50)
turnRight(ricardo)
forward(ricardo,100)

penUp(ricardo)
turnLeft(ricardo)
forward(ricardo,25)

#Draws the number 2
ricardo.setPenColor(black)
penDown(ricardo)
forward(ricardo,50)
turn(ricardo,180)
forward(ricardo,50)
turnRight(ricardo)
forward(ricardo,50)
turnRight(ricardo)
forward(ricardo,50)
turnLeft(ricardo)
forward(ricardo,50)
turnLeft(ricardo)
forward(ricardo,50)