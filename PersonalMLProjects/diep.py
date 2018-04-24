import time
import cv2
import mss
import numpy as np


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 120, 'left': 0, 'width': 960, 'height': 690}
    param1 = 100
    param2 = 14
    low = 70

    cv2.namedWindow('Sliders')
    cv2.createTrackbar('param1', 'Sliders', param1, 100, lambda x:x)
    cv2.createTrackbar('param2', 'Sliders', param2, 100, lambda x:x)
    cv2.createTrackbar('low', 'Sliders', low, 255, lambda x:x)
    while True:
        last_time = time.time()
        time.sleep(0.1)

        param1 = cv2.getTrackbarPos('param1', 'Sliders')
        param2 = cv2.getTrackbarPos('param2', 'Sliders')
        low = cv2.getTrackbarPos('low', 'Sliders')

        img = np.array(sct.grab(monitor))
        cv2.rectangle(img, (50,640), (120,550), (0,0,0), thickness=70)
        cv2.rectangle(img, (960,0), (840,80), (0,0,0), thickness=70)

        newImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        newImg = cv2.inRange(newImg, low, 160)
        if newImg is not None:
            circles = cv2.HoughCircles(
                newImg,
                cv2.HOUGH_GRADIENT,
                dp=1,
                minDist=7,
                param1=param1, param2=param2,
                minRadius=1, maxRadius=30)

        if circles is None:
            print('No Circles detected')
        else:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                # draw the outer circle
                cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
                cv2.circle(img, (i[0], i[1]), 2, (0, 255, 120), 3)

        cv2.imshow('original', img)
        cv2.imshow('circles', newImg)
        cv2.moveWindow('original', 1000, 40)
        cv2.moveWindow('circles', 1000, 1000)
        print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
cv2.destroyAllWindows()