def get_pic():
    return makePicture(pickAFile())

path = "F:/Programing/CSUMB/CSUMBfolio/CST205/FolioSite/"

def artify():
  file = pickAFile()
  pic = makePicture(file)
  for p in getPixels(pic):
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)

    if(r < 64): setRed(p, 31)
    elif(r>63 and r<128): setRed(p, 95)
    elif(r>127 and r < 192): setRed(p, 159)
    else: setRed(p, 223)

    if(g < 64): setGreen(p, 31)
    elif(g>63 and g<128): setGreen(p, 95)
    elif(g>127 and g < 192): setGreen(p, 159)
    else: setGreen(p, 223)

    if(b < 64): setBlue(p, 31)
    elif(b>63 and b<128): setBlue(p, 95)
    elif(b>127 and b < 192): setBlue(p, 159)
    else: setBlue(p, 223)
  writePictureTo(pic, path + "artify.jpg")
  show(pic)

def betterBnW(pic):
  pixels = getPixels(pic)
  for px in getPixels(pic):
    r = getRed(px)
    g = getGreen(px)
    b = getBlue(px)
    avg = (r*0.299 + g*0.587 + b*0.114)
    luminanceColors = makeColor(avg,avg,avg)
    setColor(px, luminanceColors)
  writePictureTo(pic, path + "bnw.jpg")
  repaint(pic)

def makeNegative(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = 255 - getRed(p)
    b = 255 - getBlue(p)
    g = 255 - getGreen(p)
    setRed(p, r)
    setGreen(p, g)
    setBlue(p, b)
  writePictureTo(pic, path + "negative.jpg")
  repaint(pic)

def roseColoredGlasses(pic):
  pixels = getPixels(pic)
  for p in pixels:
    #Boost Red lower others
    r = getRed(p) + 50
    b = getBlue(p) - 50
    g = getGreen(p) - 50
    #Prevent Overflow/Underflow
    if r > 255: r = 255
    if b < 0: b = 0
    if g < 0: g = 0
    setRed(p, r)
    setGreen(p, g)
    setBlue(p, b)
  writePictureTo(pic, path + "rose.jpg")
  repaint(pic)

def mirrorHorizontalTop(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range (0, width):
     for y in range (0, height/2):
       setColor(getPixel(pic, x, height-y-1), getColor(getPixel(pic,x, y)))
  writePictureTo(pic, path + "mirror.jpg")
  show(pic)

def shrink(mypic):
  width = int(getWidth(mypic)/2)
  height = int(getHeight(mypic)/2)
  pic = makeEmptyPicture(width, height)
  for x in range (0, width):
    for y in range (0, height):
       setColor(getPixel(pic, x, y), getColor(getPixel(mypic, x*2, y*2)))
  show(pic)
  writePictureTo(pic, path + "shrink.jpg")
  return pic