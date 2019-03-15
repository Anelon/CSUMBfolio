#Sample Code
def get_pic():
    file = pickAFile()
    print(file)
    return makePicture(file)

def mirrorVerticalRight():
    mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width/2):
        for y in range (0, height):
            setColor(getPixel(mypic, x, y), getColor(getPixel(mypic,width-x-1, y)))
    repaint(mypic)

def mirrorVerticalLeft():
    mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width/2):
        for y in range (0, height):
            setColor(getPixel(mypic, width-x-1, y), getColor(getPixel(mypic,x, y)))
    repaint(mypic)

def mirrorHorizontalBottom():
    mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width):
        for y in range (0, height/2):
            setColor(getPixel(mypic, x, y), getColor(getPixel(mypic,x, height-y-1)))
    file = "/Volumes/HDD/Programing/CSUMB/CSUMBfolio/CST205/Lab4/temp.JPG"
    writePictureTo(mypic, file)
    repaint(mypic)

def mirrorHorizontalTop():
    mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width):
        for y in range (0, height/2):
            setColor(getPixel(mypic, x, height-y-1), getColor(getPixel(mypic,x, y)))
    repaint(mypic)

def mirrorAll():
    mypic = get_pic();
    width = getWidth(mypic)
    height = getHeight(mypic)
    for x in range (0, width/2):
        for y in range (0, height/2):
            setColor(getPixel(mypic, width-x-1, y), getColor(getPixel(mypic, x, y)))
            setColor(getPixel(mypic, x, height-y-1), getColor(getPixel(mypic, x, y)))
            setColor(getPixel(mypic, width-x-1, height-y-1), getColor(getPixel(mypic, x, y)))
    repaint(mypic)

def simpleCopy(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    pic = makeEmptyPicture(width, height)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, x, y), getColor(getPixel(mypic, x, y)))
    show(pic)
    return pic

def rotatePic(mypic):
    width = getWidth(mypic)
    height = getHeight(mypic)
    pic = makeEmptyPicture(height, width)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, y, width-x-1), getColor(getPixel(mypic, x, y)))
    show(pic)
    return pic

def shrink(mypic):
    width = int(getWidth(mypic)/2)
    height = int(getHeight(mypic)/2)
    pic = makeEmptyPicture(width, height)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, x, y), getColor(getPixel(mypic, x*2, y*2)))
    show(pic)
    return pic
