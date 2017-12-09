#Valo Mara
#vmara2
#CS 111 Lab Monday at 3:00
#Writing text on pictures

file = pickAFile()
pic = makePicture(file)

addText(pic,20,(getHeight(pic)-20),"...What?",white)

pic.show()

writePictureTo(pic,file)

#-5 for not re-prompting for a new filename to save new picture. Program saves by overwriting original picture.