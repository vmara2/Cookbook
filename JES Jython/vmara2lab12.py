#Valo Mara
#vmara2
#CS111
#Lab 12
#Monday at 3:00PM
#Increasing and decreasing volume according to time

def makeSoundByte(sound1, start, end):
  
  sound2 = makeEmptySound(end - start)
  
  samples1 = getSamples(sound1)
  samples2 = getSamples(sound2)
  
  for i in range(0, end-start, 1):
    value1 = getSampleValue(samples1[i + start])
    setSampleValue(samples2[i], value1)
    
  return sound2
  
def modifyVolume(sound1, integer):
  
  samplelist = getSamples(sound1)

  for i in range(0, getLength(sound1), 1):
  
     soundsample = samplelist[i]
     soundvalue = getSampleValue(soundsample)
   
     if (soundvalue > 32767): #These two if statements ensures that there's no clipping of the sound file
       soundvalue = 32767
     
     if (soundvalue < -32768):
       soundvalue = -327678
     
     setSampleValue(soundsample, soundvalue*(float(integer)/100))# Here, the sound file changes according the user input
     
  return sound1
  
def joinSounds(sound1, sound2):
  
  s1List = getSamples(sound1)
  s2List = getSamples(sound2)
  
  s1Length = getLength(sound1)
  s2Length = getLength(sound2)
  
  newSound = makeEmptySound(s1Length + s2Length)
  
  newList = getSamples(newSound)

  posI = 0
  for i in range(0, s1Length, 1):
    sampleValue = getSampleValue(s1List[i])
    setSampleValue(newList[posI], sampleValue)
    posI += 1
    
  for j in range(0, s2Length, 1):
    sampleValue = getSampleValue(s2List[j])
    setSampleValue(newList[posI], sampleValue)
    posI += 1
    
  return newSound
  
def checkLength(sound):
  length = getDuration(sound)
  
  if (length<6):
    print("Error: Sound file is less than 6 seconds. Your sound file must be at least 6 seconds or longer")
    
def main():
  fname1 = pickAFile()
  
  snd1 = makeSound(fname1)
  
  checkLength(snd1)
  
  sr = getSamplingRate(snd1)
  print(sr)
  
  x = getDuration(snd1)
  
  s1 = makeSoundByte(snd1, 0, int(1*sr))
  s1 = modifyVolume(s1,25)
  s2 = makeSoundByte(snd1, int(1*sr), int(2*sr))
  s2 = modifyVolume(s2, 50)
  s3 = makeSoundByte(snd1, int(2*sr), int(3*sr))
  s3 = modifyVolume(s3, 75)
  
  s = joinSounds(s1, s2)
  s = joinSounds(s, s3)
  
  s4 = makeSoundByte(snd1, int(3*sr), int(x-(3*sr)))
  s4 = modifyVolume(s4, 100)
  
  s = joinSounds(s, s4)
  
  s5 = makeSoundByte(snd1, int(x-(3*sr)), int(x-(2*sr)))
  s5 = modifyVolume(s5, 75)
  s6 = makeSoundByte(snd1, int(x-(2*sr)), int(x-(1*sr)))
  s6 = modifyVolume(s6, 50)
  s7 = makeSoundByte(snd1, int(x-(1*sr)), int(x))
  s7 = modifyVolume(s7, 25)
  
  s = joinSounds(s, s5)
  s = joinSounds(s, s6)
  s = joinSounds(s, s7)
  
  explore(s)
  
  fname2 = pickAFile()
  writeSoundTo(s, fname2)
  
main()

#[-5] code error because you are using x as duration of sound as opposed to total length of sample. Other implementations look good