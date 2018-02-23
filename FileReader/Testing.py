import png


def box(x, y, x2, y2, picu, wid):
    for i in range(x, x2+1):
        for j in range(y, y2+1):
            pixPos = (i + 3*j*wid)
            if ((i == y) or (i == y2)):
                print([picu[pixPos], picu[pixPos + 1], picu[pixPos + 2]])
                picu[pixPos + 0] = 0
                picu[pixPos + 1] = 255
                picu[pixPos + 2] = 255

            if ((j == x) or (j == x2)):
                picu[pixPos + 0] = 0
                picu[pixPos + 1] = 255
                picu[pixPos + 2] = 255

    return picu

##############Reading from File#######################
f1 = open('images/pic05.png')

r = png.Reader(f1)
pic = r.read_flat()
width = pic[0]
height = pic[1]
picture = pic[2].tolist()
print(pic[3])
picO = picture
f1.close()

###############Writing to File#####################
edited = box(10, 10, 100, 100, picture, width)

f1 = open('images/temp.png', 'wb')
w = png.Writer(width, height, greyscale=False, bitdepth=8, alpha=True, planes=4, interlace=False)
w.write_array(f1, edited)
