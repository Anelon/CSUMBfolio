#Sample Code
def get_pic():
  return makePicture(pickAFile())

def simpleBigger(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    startW = width/2
    startH = height/2
    pic = makeEmptyPicture(width*2, height*2)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, startW+x, startH+y), getColor(getPixel(mypic, x, y)))
    show(pic)
    return pic

def pyCopy(src, target, targetX, targetY):
    width = getWidth(src)
    height = getHeight(src)
    #prevent image from going over the edge
    if targetY < 0: targetY = 0
    if targetX+width >= getWidth(target): width = getWidth(target)-targetX-1
    if targetY+height >= getHeight(target): height = getHeight(target)-targetY-1
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(target, targetX+x, targetY+y), getColor(getPixel(src, x, y)))
            #else: start overlap calculations
    #show(target)
    return target

#failed function didn't use
def lowerHighs(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width):
        for y in range (0, height):
            p = getPixel(mypic, x, y)
            r = getRed(p)
            g = getGreen(p)
            b = getBlue(p)
            sum = (r + g + b)/3
            high = 200
            top = 255-high
            if sum > high:
                over = sum-high
                lower = 1 - float(sum-high)/(top)
                r = r - over * lower
                g = g - over * lower
                b = b - over * lower
                setColor(p, makeColor(r,g,b))
    #explore(mypic)

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
    #repaint(pic)

def mirrorVerticalRight(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width/2):
        for y in range (0, height):
            setColor(getPixel(mypic, x, y), getColor(getPixel(mypic,width-x-1, y)))
    return mypic

def rotate(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    pic = makeEmptyPicture(height, width)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, y, width-x-1), getColor(getPixel(mypic, x, y)))
    #mypic = pic
    return pic

def artify(pic):
    width = getWidth(pic)
    height = getHeight(pic)
    for x in range (0, width):
        for y in range (0, height):
            p = getPixel(pic, x, y)
            r = getRed(p)
            g = getGreen(p)
            b = getBlue(p)
            if r < 64: r = 32
            elif r < 128: r = 96
            elif r < 192: r = 160
            else: r = 220
            if g < 64: g = 32
            elif g < 128: g = 96
            elif g < 192: g = 160
            else: g = 220
            if b < 64: b = 32
            elif b < 128: b = 96
            elif b < 192: b = 160
            else: b = 220
            setColor(p, makeColor(r,g,b))
    #repaint(pic)

def mirrorHorizontalTop(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width):
        for y in range (0, height/2):
            setColor(getPixel(mypic, x, height-y-1), getColor(getPixel(mypic,x, y)))
    #repaint(mypic)

def makeCollage():
    width = 3300
    height = 2550
    x = 0
    y = 0
    pic = makeEmptyPicture(width, height)
    pyCopy(makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\HayBack.jpg"), pic, 0, 0)
    #Make array for imgs
    imgs = []
    #first Row of imgs
    castle = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\Castle.jpg")
    imgs.append(castle)

    SkyBuild = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\SkyBuilding.jpg")
    SkyBuild = rotate(SkyBuild)
    SkyBuild = mirrorVerticalRight(SkyBuild)
    imgs.append(SkyBuild)

    Aquarium = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\Aquarium.jpg")
    imgs.append(Aquarium)

    #2nd row of imgs
    Inari = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\Inari.jpg")
    artify(Inari)
    imgs.append(Inari)

    Train = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\TrainLine.jpg")
    imgs.append(Train) #What?

    CastleBloss = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\CastleBloss.jpg")
    betterBnW(CastleBloss)
    imgs.append(CastleBloss)

    #3rd row of imgs
    Station = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\Station.jpg")
    imgs.append(Station)

    Tori = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\Tori.jpg")
    imgs.append(rotate(Tori))

    Fuji = makePicture("F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\Fuji.jpg")
    mirrorHorizontalTop(Fuji)
    imgs.append(Fuji)
    #place image
    for img in imgs:
        if(getWidth(img) > getHeight(img)): pyCopy(img, pic, x, y)
        else: pyCopy(img, pic, x, y-20)
        x += getWidth(img)
        if x >= width:
            x = 0
            y += getHeight(img) + 40 #20 for extra spacing

    explore(pic)
    writePictureTo(pic, "F:\Programing\CSUMB\CSUMBfolio\CST205\Lab5Imgs\out.jpg")
    return pic
