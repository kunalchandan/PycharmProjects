import random

# Generates sets of random X,Y Coordinates where the second is always to the right-of and below
# the first point. This was mainly for testing the FileReader class
output = open('randomTuples.txt', 'w+')

image = '"images/pic02.png"'

imgMaxX = 320
imgMaxY = 200

for i in range(100):
    numtuples = random.randint(1, 10)
    tuples = []
    for j in range(numtuples):
        x1 = random.randint(0, imgMaxX)
        y1 = random.randint(0, imgMaxY)
        x2 = random.randint(x1, imgMaxX)
        y2 = random.randint(y1, imgMaxY)
        tuples.append([x1, y1, x2, y2])
    output.write(image + str(tuples) + ';' + '\n')
output.close()
