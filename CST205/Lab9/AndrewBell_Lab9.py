def clip(source, start, end):
  rng = end - start
  rate = int(getSamplingRate(source))
  print(rate)
  short = makeEmptySound(rng, rate)
  for x in range(0, rng):
    value = getSampleValueAt(source, start+x)
    #printNow(value)
    setSampleValueAt(short, x, value)
  explore(short)
  return short
  
sound = makeSound(pickAFile())
explore(sound)
flesh = clip(sound, 50490, 62964)
explore(flesh)