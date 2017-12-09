#Valo Mara
#vmara2
#Monday at 3:00PM
#Lab 10
#Volume change according to user input

def modifySound(sound, integervalue): # This function changes the volume target sound file

  samplelist = getSamples(sound)

  for i in range(0, getLength(sound), 1):
  
     soundsample = samplelist[i]
     soundvalue = getSampleValue(soundsample)
   
     if (soundvalue > 32767): #These two if statements ensures that there's no clipping of the sound file
       soundvalue = 32767
     
     if (soundvalue < -32768):
       soundvalue = -327678
     
     setSampleValue(soundsample, soundvalue*(float(integervalue)/100))# Here, the sound file changes according the user input
   
  explore(sound)

def main():

  fname = pickAFile()

  s = makeSound(fname)

  n = requestInteger("To increase volume, please input any integer above 100. To decrease volume, input any integer below 100")

  explore(s)

  modifySound(s, n)
  
  fname2 = pickAFile()
  writeSoundTo(s, fname2)
main()

#-5 for not multiplying the soundvalue with the user number THEN checking for the clipping (larger than 32767 etc)