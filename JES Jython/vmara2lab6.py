#Valo Mara
#vmara2
#Monday at 3:00PM
#Colorscale drawing


#turnBlackGreen and turnWhiteGreen only change the color of the image

def turnBlackGreen(picture):
  for y in range (0, getHeight(picture), 1):
    for x in range (0, getWidth(picture), 1):
      p = getPixel(picture, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      
      cScale = int(r*.299+g*.587+b*.114)
      
      setRed(p, 0)
      setGreen(p, cScale)
      setBlue(p, 0)
      
def turnWhiteGreen(picture):
  for y in range (0, getHeight(picture), 1):
    for x in range (0, getWidth(picture), 1):
      p = getPixel(picture, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      
      cScale = int(r*.299+g*.587+b*.114)
      
      setRed(p, cScale)
      setGreen(p,255)
      setBlue(p, cScale)
      
#makeWhiteGreen and makeBlackGreen makes the picture and adds the color change      
      
def makeWhiteGreen():
  fname = pickAFile()
  pic = makePicture(fname)
  turnWhiteGreen(pic)
  print("Name: Valo Mara, NetID: vmara2")
  show(pic)
  fname2 = pickAFile()
  writePictureTo(pic, fname2)
      
def makeBlackGreen():
  fname = pickAFile()
  pic = makePicture(fname)
  turnBlackGreen(pic)
  print("Name: Valo Mara, NetID: vmara2")
  show(pic)
  fname2 = pickAFile()
  writePictureTo(pic, fname2)
  
makeWhiteGreen()

makeBlackGreen()