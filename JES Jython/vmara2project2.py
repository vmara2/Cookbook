#Valo Mara
#vmara2
#Monday 3:00PM
#Creating a 3D Image


#creates the cyan picture
def makeCyanPicture(pic2):
  for y in range (0, getHeight(pic2), 1):
    for x in range (0, getWidth(pic2), 1):
      
      p = getPixel(pic2, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      
      avg = int(r*.299 + g*.587 + b*.114)
      
      setRed(p, 0)
      setGreen(p, avg)
      setBlue(p, avg)

#creates the red picture            
def makeRedPicture(pic1):
 for y in range (0, getHeight(pic1), 1):
    for x in range (0, getWidth(pic1), 1):
      
      p = getPixel(pic1, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      
      avg = int(r*.299 + g*.587 + b*.114)
      
      setRed(p, avg)
      setGreen(p, 0)
      setBlue(p, 0)

      
#function superimposes cyan and red image to make 3-D image      
def threeDimensionalImage(pic1, pic2):
  
  makeRedPicture(pic1)
  makeCyanPicture(pic2)
  
  pic3 = makeEmptyPicture(getWidth(pic1), getHeight(pic1))
  
  for x in range (0, getWidth(pic1) , 1):
    for y in range (0, getHeight(pic1), 1):
      
      p1 = getPixel(pic1, x, y)
      p2 = getPixel(pic2, x, y)
      
      r = getRed(p1)
      g = getGreen(p2)
      b = getBlue(p2)
      
      p3 = getPixel(pic3, x, y)
      
      setRed(p3, r)
      setGreen(p3, g)
      setBlue(p3, b)
      
  return pic3

fname = pickAFile()
fname2 = pickAFile()

pic1 = makePicture(fname)
pic2 = makePicture(fname2)


#checks if the image is the correct size
if (getWidth(pic1) != getWidth(pic2)):
  
  print("Images need to be the same size!!!")
  
  fname = pickAFile()
  fname2 = pickAFile()
  
  pic1 = makePicture(fname)
  pic2 = makePicture(fname2)
  
elif (getHeight(pic1) != getHeight(pic2)):
  
  print("Images need to be the same size!!!")
  
  fname = pickAFile()
  fname2 = pickAFile()
  
  pic1 = makePicture(fname)
  pic2 = makePicture(fname2)
  
else: 
  
  newPic = threeDimensionalImage(pic1, pic2)
  
  show(newPic)