#Valo Mara
#vmara2
#Monday at 3:00
#Drawing a spirograph on a picture


filename = pickAFile()
pict = makePicture(filename)
t = makeTurtle(pict)


t.setPenColor(yellow)
t.setPenWidth(3)

turn(t, 18)

def drawStar():
  sideCount = 1
  while (sideCount <= 5):
    forward(t)
    forward(t)
    turn(t, (720/5))
    sideCount = sideCount + 1
    
def drawSpirograph():
  loopCount = 1
  while (loopCount <= 10):
    drawStar()
    turn(t,(360/10))
    loopCount = loopCount + 1

drawSpirograph()    

pict.show()


#-5 for not taking turtle as a parameter 

