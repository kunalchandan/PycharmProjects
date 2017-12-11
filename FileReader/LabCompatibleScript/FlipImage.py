import cv2
import numpy as np

def file_len(fname):
    with open(fname) as f:
        for fileEnumerator, l in enumerate(f):
            pass
    return fileEnumerator + 1


for i in range(file_len('images/index.txt')):
    image = cv2.imread('images/pic0' + str(i+1) + '.png', cv2.IMREAD_COLOR)
    print image
    imgShape = np.shape(image)
    wid = imgShape[0]
    height = imgShape[1]
    angle = 30
    rad = np.deg2rad(angle)

    newWid = np.abs(np.sin(rad) * wid) + np.abs(np.cos(rad) * height)
    newHeight = (np.abs(np.cos(rad) * wid) + np.abs(np.sin(rad) * height))

    rotationMatrix = cv2.getRotationMatrix2D((newWid/2, newHeight/2), angle, 1)
    rotationMove = np.dot(rotationMatrix, np.array([(newWid-wid)/2, (newHeight-height)/2, 0]))
    rotationMatrix[0, 2] += rotationMove[0]
    rotationMatrix[1, 2] += rotationMove[1]
    rotated = cv2.warpAffine(image, rotationMatrix, (int(np.ceil(newWid)), int(np.ceil(newHeight))), flags=cv2.INTER_LANCZOS4)
    cv2.imwrite(('images/rotImgs/' + str(i+1) + '.png'), rotated)

for i in range(file_len('images/index.txt')):
    image = cv2.imread('images/pic0' + str(i+1) + '.png', cv2.IMREAD_COLOR)
    flipped = cv2.flip(image, 1)
    cv2.imwrite(('images/flipImgs/' + str(i+1) + '.png'), flipped)
