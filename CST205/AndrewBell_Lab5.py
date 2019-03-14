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
    if targetX+width > getWidth(target): width = getWidth(target)
    if targetY+height > getHeight(target): height = getHeight(target)
    for x in range (0, width):
        for y in range (0, height):
            setColor(getPixel(pic, targetX+x, targetY+y), getColor(getPixel(mypic, x, y)))
    show(pic)
    return pic

def makeCollage():
    width = 2550
    height = 3300
