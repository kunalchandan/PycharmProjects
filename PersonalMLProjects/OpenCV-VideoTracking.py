import numpy as np
import cv2
import time


def prgb(one, two, three, four, five):
    print two
    print three


def hi(x):
    x = x
    pass


hue, sat, val, hue1, sat1, val1 = [0, 190, 60, 255, 255, 255] # tracks red cup rn
param1 = 100
param2 = 93
other1 = 35
other2 = 90
cap = cv2.VideoCapture(0)
cv2.namedWindow('Sliders')
cv2.createTrackbar('Hue', 'Sliders', hue, 255, hi)
cv2.createTrackbar('Sat', 'Sliders', sat, 255, hi)
cv2.createTrackbar('Val', 'Sliders', val, 255, hi)
cv2.createTrackbar('Hue1', 'Sliders', hue1, 255, hi)
cv2.createTrackbar('Sat1', 'Sliders', sat1, 255, hi)
cv2.createTrackbar('Val1', 'Sliders', val1, 255, hi)
cv2.createTrackbar('param1', 'Sliders', param1, 100, hi)
cv2.createTrackbar('param2', 'Sliders', param2, 100, hi)
cv2.createTrackbar('other1', 'Sliders', other1, 100, hi)
cv2.createTrackbar('other2', 'Sliders', other2, 100, hi)
cv2.moveWindow('Sliders', 0, 0)
while True:
    # Capture frame-by-frame
    if cap.grab():
        ret, frame = cap.retrieve()
    else:
        print 'Failed to load image'

    cv2.setMouseCallback('Original', prgb)

    # Capture HSV values and redefine filter
    hue = cv2.getTrackbarPos('Hue', 'Sliders')
    sat = cv2.getTrackbarPos('Sat', 'Sliders')
    val = cv2.getTrackbarPos('Val', 'Sliders')
    hue1 = cv2.getTrackbarPos('Hue1', 'Sliders')
    sat1 = cv2.getTrackbarPos('Sat1', 'Sliders')
    val1 = cv2.getTrackbarPos('Val1', 'Sliders')
    other1 = cv2.getTrackbarPos('other1', 'Sliders')
    other2 = cv2.getTrackbarPos('other2', 'Sliders')
    param1 = cv2.getTrackbarPos('param1', 'Sliders')
    param2 = cv2.getTrackbarPos('param2', 'Sliders')
    low = np.array([hue, sat, val])
    up = np.array([hue1, sat1, val1])

    # Frame operations
    newFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(newFrame, low, up)
    circles = cv2.HoughCircles(
        mask,
        cv2.HOUGH_GRADIENT,
        other1,
        other2,
        param1=param1,
        param2=param2,
        minRadius=20,
        maxRadius=100
    )
    if circles is None:
        print 'No Circles detected'
    else:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(newFrame, (i[0], i[1]), i[2], (0, 0, 255), 2)
            # draw the center of the circle
            cv2.circle(newFrame, (i[0], i[1]), 2, (255, 120, 120), 3)

    # Display the resulting frame
    cv2.imshow('HSV Mask', mask)
    cv2.imshow('Original', frame)
    cv2.imshow('HSV Converted', newFrame)
    cv2.moveWindow('HSV Mask', 400, 0)
    cv2.moveWindow('Original', 1200, 0)
    cv2.moveWindow('HSV Converted', 1700, 500)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
