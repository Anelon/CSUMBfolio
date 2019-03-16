#Sample Code
def get_pic():
    file = pickAFile()
    print(file)
    return makePicture(file)

def mirrorVerticalRight(mypic):
    #mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width/2):
        for y in range (0, height):
            setColor(getPixel(mypic, x, y), getColor(getPixel(mypic,width-x-1, y)))
    writePictureTo(mypic, "F:\Programing\CSUMB\CSUMBfolio\CST205\Lab4\mirrorVertRight.jpg")
    repaint(mypic)

def mirrorVerticalLeft(mypic):
    #mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width/2):
        for y in range (0, height):
            setColor(getPixel(mypic, width-x-1, y), getColor(getPixel(mypic,x, y)))
    repaint(mypic)

def mirrorHorizontalBottom(mypic):
    #mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width):
        for y in range (0, height/2):
            setColor(getPixel(mypic, x, y), getColor(getPixel(mypic,x, height-y-1)))
    writePictureTo(mypic, "F:\Programing\CSUMB\CSUMBfolio\CST205\Lab4\mirrorHorizontalBot.jpg")
    repaint(mypic)

def mirrorHorizontalTop(mypic):
    #mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width):
        for y in range (0, height/2):
            setColor(getPixel(mypic, x, height-y-1), getColor(getPixel(mypic,x, y)))
    writePictureTo(mypic, "F:\Programing\CSUMB\CSUMBfolio\CST205\Lab4\mirrorHorizontalTop.jpg")
    repaint(mypic)

def mirrorAll(mypic):
    #mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width/2):
        for y in range (0, height/2):
            setColor(getPixel(mypic, width-x-1, y), getColor(getPixel(mypic, x, y)))
            setColor(getPixel(mypic, x, height-y-1), getColor(getPixel(mypic, x, y)))
            setColor(getPixel(mypic, width-x-1, height-y-1), getColor(getPixel(mypic, x, y)))
    writePictureTo(mypic, "F:\Programing\CSUMB\CSUMBfolio\CST205\Lab4\mirrorQuad.jpg")
    repaint(mypic)

def simpleCopy(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    pic = makeEmptyPicture(width, height)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, x, y), getColor(getPixel(mypic, x, y)))
    return pic

def rotatePic(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    pic = makeEmptyPicture(height, width)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, y, width-x-1), getColor(getPixel(mypic, x, y)))
    show(pic)
    #this does not work (need "\\" before character r, t, n possibly others)
    #writePictureTo(pic, "F:\Programing\CSUMB\CSUMBfolio\CST205\Lab4\rotate.jpg")
    #this does
    writePictureTo(pic, "F:\Programing\CSUMB\CSUMBfolio\CST205\Lab4\\rotate.jpg")
    return pic

def shrink(mypic):
    width = int(getWidth(mypic)/2)
    height = int(getHeight(mypic)/2)
    pic = makeEmptyPicture(width, height)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, x, y), getColor(getPixel(mypic, x*2, y*2)))
    show(pic)
    writePictureTo(pic, "F:\Programing\CSUMB\CSUMBfolio\CST205\Lab4\shrink.jpg")
    return pic

def runAll():
    pic = get_pic()
    shrink(simpleCopy(pic))
    rotatePic(simpleCopy(pic))
    mirrorVerticalRight(simpleCopy(pic))
    mirrorHorizontalBottom(simpleCopy(pic))
    mirrorHorizontalTop(simpleCopy(pic))
    mirrorAll(simpleCopy(pic))
