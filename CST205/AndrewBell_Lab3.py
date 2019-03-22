#Sample Code
def get_pic():
    return makePicture(pickAFile())

def halfRed():
    pic = get_pic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        setRed(p, r*0.5)
    repaint(pic)

def noBlue():
    pic = get_pic()
    pixels = getPixels (pic)
    for p in pixels:
        b = getBlue(p)
        setBlue (p, b * 0)
    repaint (pic)

#Problem 1
def lessRed(amount):
    pic = get_pic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        setRed(p, r*((100 - amount)/100.0))
    repaint(pic)

def halfRed2():
    lessRed(50)

#Problem 2
def moreRed(amount):
    pic = get_pic()
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        newRed = r * ((100 + amount)/100.0)
        if newRed > 255: newRed = 255 #prevent overflow
        setRed(p, newRed)
    repaint(pic)

#Problem 3
def roseColoredGlasses():
    pic = get_pic()
    pixels = getPixels(pic)
    for p in pixels:
        #Boost Red lower others
        r = getRed(p) + 50
        b = getBlue(p) - 50
        g = getGreen(p) - 50
        #Prevent Color Overflow/Underflow
        if r > 255: r = 255
        if b < 0: b = 0
        if g < 0: g = 0

        setRed(p, r)
        setGreen(p, g)
        setBlue(p, b)

    repaint(pic)

#Problem 4
def lightenUp():
    pic = get_pic()
    pixels = getPixels(pic)
    for p in pixels:
        color = getColor(p)
        newColor = makeLighter(color)
        setColor(p, newColor)
    repaint(pic)

#Problem 5
def makeNegative():
    pic = get_pic()
    pixels = getPixels(pic)
    for p in pixels:
        r = 255 - getRed(p)
        b = 255 - getBlue(p)
        g = 255 - getGreen(p)
        setRed(p, r)
        setGreen(p, g)
        setBlue(p, b)
    repaint(pic)

#Problem 6:
def BnW():
    pic = get_pic()
    pixels = getPixels(pic)
    for px in getPixels(pic):
        r = getRed(px)
        g = getGreen(px)
        b = getBlue(px)
        average = (r+g+b)/3.0
        new_color = makeColor (average,average,average)
        setColor(px, new_color)
    repaint(pic)

def betterBnW():
    pic = get_pic()
    pixels = getPixels(pic)
    for px in getPixels(pic):
        r = getRed(px)
        g = getGreen(px)
        b = getBlue(px)
        avg = (r*0.299 + g*0.587 + b*0.114)
        luminanceColors = makeColor(avg,avg,avg)
        setColor(px, luminanceColors)
    repaint(pic)

