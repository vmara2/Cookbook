#Valo Mara
#vmara2
#Monday at 3PM
#Rotating image based on user input
  
def rotate90():
  picB = makeEmptyPicture(getHeight(picA),getWidth(picA)) #makes converts height into the width and vice versa
  
  for x in range(0, getWidth(picA)):
    for y in range(0, getHeight(picA)):
      p = getPixel(picA, x, y)
      color = getColor(p)
      mirrorp = getPixel(picB, getHeight(picA) - 1 - y, x)
      setColor(mirrorp, color)
          
  show(picB)
  return(picB) #Needs to return pic in order to save picture to a file
  #Following functions follow similar structure

def rotate180():
  picB = makeEmptyPicture(getWidth(picA),getHeight(picA))
  
  for x in range(0, getWidth(picA)):
    for y in range(0, getHeight(picA)):
      p = getPixel(picA, x, y)
      color = getColor(p)
      mirrorp = getPixel(picB, getWidth(picA) - 1 - x, getHeight(picA) - 1 - y)
      setColor(mirrorp, color)
          
  show(picB)
  return(picB)

def rotate270():
  picB = makeEmptyPicture(getHeight(picA),getWidth(picA))
  
  for x in range(0, getWidth(picA)):
    for y in range(0, getHeight(picA)):
      p = getPixel(picA, x, y)
      color = getColor(p)
      mirrorp = getPixel(picB, y, getWidth(picA) - 1 - x)
      setColor(mirrorp, color)
          
  show(picB)
  return(picB)

print("Valo Mara")
print("vmara2")

fname = pickAFile()
picA = makePicture(fname)

value = requestIntegerInRange("Please enter a number 1-3", 1,3)

if (value == 1):
    newPic = rotate90()
elif value == 2:
    newPic = rotate180()
elif value == 3:
    newPic = rotate270()
else:
    requestIntegerInRange("Number not in range. Please enter a number 1-3", 1, 3)

fname2 = pickAFile()
writePictureTo(newPic, fname2)

