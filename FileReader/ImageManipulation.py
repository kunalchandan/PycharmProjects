import cv2
import numpy as np


def rotate(path, imgname, angle):
    image = cv2.imread(path + imgname, cv2.IMREAD_COLOR)
    imgShape = np.shape(image)
    wid = imgShape[0]
    height = imgShape[1]
    rad = np.deg2rad(angle)

    newWid = np.abs(np.sin(rad) * wid) + np.abs(np.cos(rad) * height)
    newHeight = (np.abs(np.cos(rad) * wid) + np.abs(np.sin(rad) * height))

    rotationMatrix = cv2.getRotationMatrix2D((newWid/2, newHeight/2), angle, 1)
    rotationMove = np.dot(rotationMatrix, np.array([(newWid-wid)/2, (newHeight-height)/2, 0]))
    rotationMatrix[0, 2] += rotationMove[0]
    rotationMatrix[1, 2] += rotationMove[1]
    rotated = cv2.warpAffine(
        image,
        rotationMatrix,
        ( int(np.ceil(newWid)), int(np.ceil(newHeight)) ),
        flags=cv2.INTER_LANCZOS4
        )
    cv2.imwrite((path + 'rotImgs/' + imgname), rotated)


def darken(path, imgname, amount):
    image = cv2.imread(path + imgname, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    value = hsv[:, :, 2]
    newV = np.where((255 - value) < amount, 255, value + amount)
    hsv[:, :, 2] = newV

    newimage = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    cv2.imwrite((path + 'darkImgs/' + imgname), newimage)


def flipYaxis(path, imgname):
    image = cv2.imread(path + imgname, cv2.IMREAD_COLOR)
    flipped = cv2.flip(image, 1)
    cv2.imwrite((path + 'flipImgs/' + imgname), flipped)


def flipXaxis(path, imgname):
    image = cv2.imread(path + imgname, cv2.IMREAD_COLOR)
    flipped = cv2.flip(image, 0)
    cv2.imwrite((path + 'flipImgs/' + imgname), flipped)


flipYaxis('images/', 'pic03.png')
flipXaxis('images/', 'pic03.png')
rotate('images/', 'pic03.png', 10)
darken('images/', 'pic03.png', -100)
cv2.imshow('dark', cv2.imread('images/darkImgs/pic03.png'))
cv2.imshow('flip', cv2.imread('images/flipImgs/pic03.png'))
cv2.imshow('rot', cv2.imread('images/rotImgs/pic03.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()