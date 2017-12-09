#Valo Mara
#vmara2
#Monday at 3:00OPM
#Posterizing a picture

fname = pickAFile()
pic = makePicture(fname)

def posterize(picture):
  for x in range(0, getWidth(picture), 1):
    for y in range(0, getHeight(picture), 1):
      #gets the gray value of the picture
      p = getPixel(picture, x, y) 
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      avg = int(r*.299+g*.587+b*.114)
      
      #sets pixel to medium violet pink
      if (avg < 42):
        setRed(p,199) 
        setGreen(p,21)
        setBlue(p,133)
      #sets pixel to deep pink
      elif (avg < 84):
        setRed(p, 255)
        setGreen(p, 20)
        setBlue(p, 147)
      #sets pixel to violet
      elif (avg < 128):
        setRed(p, 238)
        setGreen(p, 130)
        setBlue(p, 238)
      #sets pixel to hot pink
      elif (avg < 170):
        setRed(p, 255)
        setGreen(p, 105)
        setBlue(p, 180)
      #sets pixel to light pink
      elif (avg < 212):
        setRed(p, 255)
        setGreen(p, 182)
        setBlue(p, 193)
      #sets remaining pixels to pink
      else: 
        setRed(p, 255)
        setGreen(p, 192)
        setBlue(p, 203)

posterize(pic)
show(pic)