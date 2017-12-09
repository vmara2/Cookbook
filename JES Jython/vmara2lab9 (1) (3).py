#Valo Mara
#vmara2
#Monday at 3:00PM
#Duplicating image based on user input

#Makes duplicates of input picture based on user's input
#returns a picture containing the duplicates
def duplicate(picture, numDupes):
  outputpic = makeEmptyPicture(getWidth(picture), getHeight(picture) * numDupes) 
  
  for c in range(0, numDupes, 1): #c determines how many times to run loop based on the user input
    for x in range(0, getWidth(picture), 1):
      for y in range(0, getHeight(picture), 1):
        inputpix = getPixel(picture, x, y)
        color = getColor(inputpix)
        
        newx = x
        newy = y + getHeight(picture) * c 
                
        outputpix = getPixel(outputpic, newx, newy) #duplicate picture placement based on the value of c
        setColor(outputpix, color)
       
  return outputpic #returns final picture
  
fname = pickAFile()
pic = makePicture(fname)

value = requestIntegerInRange("Please enter an integer between 1 and 10",1,10) #requests interger from user
print("The user entered: " + str(value))

newpic = duplicate(pic, value)
show(newpic) #shows the picture returned from the duplicate function

fname2 = pickAFile()
writePictureTo(newpic, fname2)