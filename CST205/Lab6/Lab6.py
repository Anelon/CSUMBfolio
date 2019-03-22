
#CST 205
#Lab 6
#SAGA (Team 2)

#Helper
def get_pic():
    return makePicture(pickAFile())

#Problem warmup: Redeye function

def redEye():
    file = pickAFile()
    pic = makePicture(file)
    for p in getPixels(pic):
         if distance(makeColor(178, 0, 0), getColor(p)) < 120:
            setColor(p, black)
    repaint(pic)
    return pic

#Problem 1

#Legacy code for sepia
def betterBnW(pic):
    width = getWidth(pic)
    height = getHeight(pic)
    for x in range (0, width):
        for y in range (0, height):
            px = getPixel(pic, x, y)
            r = getRed(px)
            g = getGreen(px)
            b = getBlue(px)
            avg = (r*0.299 + g*0.587 + b*0.114)
            luminanceColors = makeColor(avg,avg,avg)
            setColor(px, luminanceColors)


#This function applies a sepia filter to a picture.
#Calls betterBnW

def sepia():
  file = pickAFile()
  pic = makePicture(file)
  betterBnW(pic)
  
  for p in getPixels(pic): 
    Red = getRed(p)
    Green = getGreen(p)
    Blue = getBlue(p)
    
    if Red<63:
      setRed(p, Red*1.1)
      setBlue(p, Blue*0.9)
    elif 62 < Red < 192:
      setRed(p, Red*1.15)
      setBlue(p, Blue*0.85)
    elif 191<Red:
     setRed(p, Red*1.08)
     setBlue(p, Blue*0.93 )
    else:
     setRed(p, 255)
  
  repaint(pic)
 
  return pic

#Problem 2

#This function "artify"s a the picture chosen. The result is displayed.

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
  show(pic)


#Problem 3 

#Helper function. Separated from chromakey in order to maintain
#good design practices/code reusability

def greenCopy(src, target, targetX, targetY):
    width = getWidth(src)
    height = getHeight(src)
    #prevent image from going over the edge
    if targetY < 0: targetY = 0
    if targetX < 0: targetX = 0
    if targetX+width >= getWidth(target): width = getWidth(target)-targetX-1
    if targetY+height >= getHeight(target): height = getHeight(target)-targetY-1
    for x in range (0, width):
        for y in range (0, height):
            p = getPixel(src, x, y)
            if distance(makeColor(86, 225, 10), getColor(p)) > 125 and distance(makeColor(43, 216, 39), getColor(p)) > 120:
              setColor(getPixel(target, targetX+x, targetY+y), getColor(getPixel(src, x, y)))
    return target


#This function operates on three pictures; a background
#and two greenscreen pictures.  The greenscreen pictures
#are transposed onto the background picture. The resulting
#picture is both displayed and returned.


def chromakey():
    obama = get_pic()
    trex = get_pic()
    background = get_pic()
    bottom = getHeight(background)
    right = getWidth(background)
    left = 0
    newPic = greenCopy(trex, background, left, bottom-getHeight(trex))
    newPic = greenCopy(obama, newPic, right-getWidth(obama), bottom-getHeight(obama))
    repaint(newPic)
    return newPic

