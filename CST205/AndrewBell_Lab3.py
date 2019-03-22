def get_pic():
    return makePicture(pickAFile())

def redEye(pic):
    width = getWidth(pic)
    height = getHeight(pic)
    for x in range (0, width):
        for y in range (0, height):
            px = getPixel(pic, x, y)
            r = getRed(px)
            g = getGreen(px)
            b = getBlue(px)
            if r > 200 and g < 200: r = 0 
    explore(pic)distance(

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


def artify(pic):
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

def artifyBW(pic):
    for p in getPixels(pic):
        r = getRed(p)
        b = getBlue(p)
        g = getGreen(p)
        lum = (r + g + b) / 3
        if lum < 100: setColor(p, black)
        else: setColor(p, white)
