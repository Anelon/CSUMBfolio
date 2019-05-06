def clip(source, start, end):
  rng = end - start
  rate = int(getSamplingRate(source))
  print(rate)
  short = makeEmptySound(rng, rate)
  for x in range(0, rng):
    value = getSampleValueAt(source, start+x)
    #printNow(value)
    setSampleValueAt(short, x, value)
  return short

def copy(source, target, start):
  rng = getNumSamples(source)
  rate = int(getSamplingRate(source))
  print(rate)
  if start + rng > getNumSamples(target):
    rng = (rng + start) - getNumSamples(target)
  for x in range(0, rng):
    value = getSampleValueAt(source, start+x)
    setSampleValueAt(target, x, value)

def reverse(sound):
  rng = getNumSamples(sound)
  rate = int(getSamplingRate(sound))
  rev = makeEmptySound(rng, rate)
  for x in range(0, rng):
    value = getSampleValueAt(sound, rng-x-1)
    setSampleValueAt(rev, x, value)
  return rev

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

def makeCollage():
  sound1 = makeSound(pickAFile())
  sound1Len = getNumSamples(sound1)
  rate = int(getSamplingRate(sound1))
  sound2 = makeSound(pickAFile())
  sound2Len = getNumSamples(sound2)
  sound3 = makeSound(pickAFile())
  sound3Len = getNumSamples(sound3)
  sound4 = makeSound(pickAFile())
  sound4Len = getNumSamples(sound4)
  sound5 = makeSound(pickAFile())
  sound5Len = getNumSamples(sound5)
  curr = 0
  total = sound1Len + sound2Len + sound3Len + sound4Len + sound5Len
  collage = makeEmptySound(total, rate)
  for x in range(0, sound1Len):
    value = getSampleValueAt(sound1, x)
    setSampleValueAt(collage, x + curr, value)
  curr += sound1Len -1
  explore(collage)
  for x in range(0, sound2Len):
    value = getSampleValueAt(sound2, x)
    setSampleValueAt(collage, x + curr, value)
  explore(collage)
  curr += sound2Len -1
  for x in range(0, sound3Len):
    value = getSampleValueAt(sound3, x)
    setSampleValueAt(collage, x + curr, value)
  explore(collage)
  curr += sound3Len -1
  for x in range(0, sound4Len):
    value = getSampleValueAt(sound4, x)
    setSampleValueAt(collage, x + curr, value)
  explore(collage)
  curr += sound4Len -1
  for x in range(0, sound5Len):
    value = getSampleValueAt(sound5, x)
    setSampleValueAt(collage, x + curr, value)
  explore(collage)
  curr += sound5Len -1
  maxVolume(collage)
  return collage

sound = makeSound(pickAFile())
#explore(sound)
flesh = clip(sound, 50490, 62964)
#flesh = reverse(flesh)

explore(flesh)
