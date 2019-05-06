#Xiaoran Sun, Andrew Bell
#CST 205
#lab 8

#testing functions
def main():
  sound = makeSound(pickAFile())
  decreaseVolume(sound)
  changeVolume(sound, 2.0)
  maxSample(sound)
  maxVolume(sound)
  goToEleven(sound)
  
#decreaseVolume
def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * .05)
   #writeSoundTo(sound, path)
   return sound      
      
#changeVolume
def changeVolume(sound, factor):
  for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value*factor)
      #writeSoundTo(sound, path)
  return sound
  
#maxSample
def maxSample(sound):
  max_sound = -32767
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    max_sound = max(value, max_sound)
  #writeSoundTo(sound, path)
  return sound

#bit-depth 16
def maxVolume(sound):
  maximum  = 0
  for sample in getSamples(sound):
    maximum  = max(maximum, getSampleValue(sample))
  factor = 32767/maximum
  for sample in getSamples(sound):
    max_sound = factor*getSampleValue(sample)
    setSampleValue(sample, max_sound)
  #writeSoundTo(sound, path)
  return sound
 

#goToEleven
def goToEleven(sound):
  for sample in getSamples(sound):
     value = getSampleValue(sample)
     if value >0: setSampleValue(sample, 32767)
     if value <0: setSampleValue(sample, -32768)
  #writeSoundTo(sound, path)
  return sound
    
    
    
   
  
  
  
  
  