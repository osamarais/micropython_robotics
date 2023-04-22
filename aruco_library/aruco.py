# -*- coding: utf-8 -*-
"""
Created on Fri May  4 19:37:29 2018

@author: Alper
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_FPS, 15)
#cap.set(cv2.CAP_PROP_EXPOSURE, 10)
#cap.set(cv2.CAP_PROP_CONTRAST, 90)
        
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
cameraMatrix = np.load("cam_broke_mtx.npy")
distCoeffs = np.load("cam_broke_dist.npy")


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    res = cv2.aruco.detectMarkers(gray,dictionary)
    cv2.aruco.drawAxis(frame, cameraMatrix, distCoeffs, (0,0,0), (0,0,0), 0.1)

#    print(res[0],res[1],len(res[2]))

    if len(res[0]) > 0:
        cv2.aruco.drawDetectedMarkers(frame,res[0],res[1])
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()