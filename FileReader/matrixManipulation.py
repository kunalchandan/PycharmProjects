import cv2
import numpy as np
import pandas as pd

# Same as  image manipulation, however these functions take arrays that represent images and 
# apply the same operations on them and returns them.

def rotate(array, angle):
    imgShape = np.shape(array)
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
        array,
        rotationMatrix,
        ( int(np.ceil(newWid)), int(np.ceil(newHeight)) ),
        flags=cv2.INTER_NEAREST
        )
    return rotated


def darken(array, amount):
    hsv = cv2.cvtColor(array, cv2.COLOR_RGB2HSV)
    value = hsv[:, :, 2]
    newV = np.where((255 - value) < amount, 255, value + amount)

    hsv[:, :, 2] = newV

    newimage = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    return newimage


def darkenGRAY(array, amount):
    new = np.where(((255 - array) < amount), 255, array + amount)
    low_values_flags = new < 0  # Where values are low
    new[low_values_flags] = 0
    return new


def flipYaxis(array):
    flipped = cv2.flip(image, 1)
    return flipped


def flipXaxis(path, imgname):
    flipped = cv2.flip(image, 0)
    return flipped


file = pd.read_csv('images.csv')

array = np.array(file.as_matrix())
array = np.delete(array, 0, axis=1)
image = array[0].reshape(28, 28)

rottenIMG = rotate(image, 30)
darkIMG = darkenGRAY(image, -40)

print(image)
print(rottenIMG)
print(darkIMG)
print(flipYaxis(image))

#flipYaxis('images/', 'pic03.png')
#flipXaxis('images/', 'pic03.png')
#rotate('images/', 'pic03.png', 10)
#darken('images/', 'pic03.png', -100)
cv2.waitKey(0)
cv2.destroyAllWindows()
